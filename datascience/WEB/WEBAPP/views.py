from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def hi(request):
    return HttpResponse('<h1>THIS IS MY WEBAPP</h1>')
