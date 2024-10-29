from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def login(request):
    return render(request,'authentication-login.html')
def signup(request):
    return render(request,'authentication-register.html')
def index(request):
    return render(request,'index.html')
def carde(request):
    return render(request,'liste.html')