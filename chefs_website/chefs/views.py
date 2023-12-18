from django.shortcuts import render
from django.http import HttpResponse

def Order(request, template_name=None):
    return render(request, 'index.html')

