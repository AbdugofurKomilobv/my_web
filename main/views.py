from django.shortcuts import render
from main.models import Portfolio

def home(request):
    portfolios = Portfolio.objects.all()
    return render(request, template_name='index.html',context={'portfolios':portfolios})

