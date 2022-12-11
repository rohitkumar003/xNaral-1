from django.urls import path
from . import views

urlpatterns = [
    path('', views.CurrencyViewSet.index, name='index'),
    path('create', views.CurrencyViewSet.create, name="create"),
    path('retrieve', views.CurrencyViewSet.retrieve, name="retrieve"),
    path('edit/<int:id>', views.CurrencyViewSet.edit, name="edit"),
    path('update/<int:id>', views.CurrencyViewSet.update, name="update"),
    path('delete/<int:id>', views.CurrencyViewSet.destroy, name="destroy"),
    path('convert/<int:id>', views.CurrencyViewSet.convert, name="convert"),
    path('calculateFX', views.CurrencyViewSet.calculateFX, name="calculateFX"),
]