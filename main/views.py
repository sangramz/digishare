from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def home(request):
    """
    DESC    : Site Landing Page
    ARGS    : No Args 
    RETURNS : Returns Main Landing Page
    """
    return render(request, 'main/dashboard.html')


def dashboard(request):
    return render(request, 'main/base.html')


def investment_plans(request):
    return render(request, 'main/investment.html')


def add_investment_plans(request):
    return render(request, 'main/add-investment.html')


def login(request):
    pass


def register(request):
    pass