from django import forms
from currency.models import CurrencyPair


class CurrencyForm(forms.ModelForm):
    class Meta:
        model = CurrencyPair
        fields = "__all__"
