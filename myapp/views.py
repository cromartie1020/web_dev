from django.shortcuts import render
from .models import Place
from . import forms
# Create your views here.
def display_article(request):
    forms=Place(request.POST)
    forms.save()
    
    return render(request,'myapp/form_demo.html',{'forms':forms})
