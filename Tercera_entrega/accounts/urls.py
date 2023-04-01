from django.urls import path
from accounts.views import registro_pasajero, login_account

urlpatterns= [
    path('registro/', registro_pasajero, name="registro"),
    path('login/', login_account, name="login")
  ]

