from django import views
from django.urls import path
from .views import CustomEmploeeLogin, dashboard, CustomerCreate

urlpatterns = [
    path('login/', CustomEmploeeLogin.as_view(), name='login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('customer-create/', CustomerCreate.as_view(), name='customer-create'),
]
