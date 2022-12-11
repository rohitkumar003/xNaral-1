from urllib.request import urlopen

from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, render

from .forms import CurrencyForm
from .models import CurrencyPair
from rest_framework.decorators import action
from django.shortcuts import render,redirect
import json

class CurrencyViewSet(viewsets.ModelViewSet):

    @action(detail=True, methods=['get'])
    def index(request):
        return render(request, 'index.html')

    def create(request):
        if request.method == "POST":
            currency_code = request.POST['currency_code']
            language = request.POST['language']
            target_currency_code = request.POST['target_currency_code']
            obj = CurrencyPair.objects.create(currency_code=currency_code, language=language, target_currency_code=target_currency_code)

            obj.save()
        return redirect('retrieve')

    def list(request):
        queryset = CurrencyPair.objects.all()
        return render(request, 'retrieve.html', {'details': queryset})

    def retrieve(request):
        queryset = CurrencyPair.objects.all()
        return render(request, 'retrieve.html', {'details': queryset})

    def edit(request, id):
        record = CurrencyPair.objects.get(id=id)
        return render(request, 'edit.html', {'record': record})

    def update(request, key):
        record = CurrencyPair.objects.get(id=key)
        form = CurrencyForm(request.POST, instance=record)
        if form.is_valid:
            form.save()
            record = CurrencyPair.objects.all()
            return redirect('retrieve')

    def destroy(request, id):
        record = CurrencyPair.objects.get(id=id)
        record.delete()

        return redirect('retrieve')

    @action(detail=True, methods=['get', 'post'])
    def convert(request, id):
        record = CurrencyPair.objects.get(id=id)
        return render(request, 'convert.html', {'record': record})

    def calculateFX(request):
        amount = request.POST['amount']
        source_currency = request.POST['currency_code']
        target_currency = request.POST['target_currency_code']
        exchange_rate_json = urlopen('https://xnara-hiring-default-rtdb.asia-southeast1.firebasedatabase.app/currencyrate.json')
        exchange_rate = json.loads(exchange_rate_json.read())


        print(exchange_rate)
