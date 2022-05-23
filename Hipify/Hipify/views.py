from django.http import HttpResponse
from django.contrib import admin
from django.shortcuts import render

def home_view(request):
    context = {
    }
    return render(request, "home.html",context)

def landing_view(request):
    return HttpResponse('<h1>Hello World</h1>')

