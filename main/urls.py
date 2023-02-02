from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('investment-plans/', views.investment_plans, name='invesment-plans'),
    path('add-investment-plans/', views.add_investment_plans, name='add-invesment-plans'),
    path('registeration/', views.register, name='register'),
]