from django.shortcuts import render # type: ignore
from django.http import HttpResponse # type: ignore

# Create your views here.
def login(request):
    return render(request,'pages/signin.html')
def signup(request):
    return render(request,'pages/signup.html')
def index(request):
    return render(request,'pages/index.html')
def carde(request):
    return render(request,'HR/contrat_list.html')