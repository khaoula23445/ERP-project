from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def login(request):
    return render(request,'pages/signin.html')
def signup(request):
    return render(request,'pages/signup.html')
def index(request):
    return render(request,'pages/index.html')
def carde(request):
    return render(request,'HR/employee_list.html')