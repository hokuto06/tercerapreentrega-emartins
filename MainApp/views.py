from django.shortcuts import render
from django.http import HttpResponse

def inicio(req):
    return render(req, 'inicio.html')