# cryptoapp/urls.py

from django.urls import path
from .views import crypto_chart, crypto_list

urlpatterns = [
    path('<str:crypto_name>/', crypto_chart, name="crypto_chart"),
    path('', crypto_list, name="crypto_list"), 
]
