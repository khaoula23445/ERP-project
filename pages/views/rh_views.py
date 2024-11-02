import json
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from pages.models import Employee, Contrat
from django.db import transaction
from django.shortcuts import render # type: ignore
from django.http import HttpResponse # type: ignore

# Create your views here.
def login(request):
    return render(request,'pages/signin.html')
def signup(request):
    return render(request,'pages/signup.html')
def index(request):
    return render(request,'pages/index.html')


def add_employee(request):
    if request.method == "POST":
        with transaction.atomic():
            # Create and save Employee
            employee = Employee(
                num_ss=request.POST.get('num_ss'),
                type=request.POST.get('type'),
                firstname=request.POST.get('firstname'),
                lastname=request.POST.get('lastname'),
                birth_date=request.POST.get('birth_date'),
                adress=request.POST.get('adress'),
                email=request.POST.get('email'),
                gendre=request.POST.get('gendre'),
                situation=request.POST.get('situation'),
                nbr_child=request.POST.get('nbr_child'),
                blood_type=request.POST.get('blood_type'),
                birth_address=request.POST.get('birth_address'),
                num_carte=request.POST.get('num_carte'),
                photo=request.POST.get('photo'),
                phone=request.POST.get('phone')
            )
            employee.save()

            # Create and save Contract linked to the Employee
            contract = Contrat(
                contrat_type=request.POST.get('contrat_type'),
                start_date=request.POST.get('start_date'),
                salary_amount=request.POST.get('salary_amount'),
                status=request.POST.get('status'),
                function=request.POST.get('function'),
                employee=employee
            )
            contract.save()

        return render(request, 'HR/add_employee.html')# Redirect to a success page after submission

    return render(request, 'HR/add_employee.html')

def show_employees_contract(request):
    # Retrieve all contracts along with their employees
    contracts = Contrat.objects.select_related('employee').all()

    active_employees = []
    inactive_employees = []

    # Organize employees based on their contract status
    for contract in contracts:
        employee_info = {
            'id': contract.employee.idemployee,
            'firstname': contract.employee.firstname,
            'lastname': contract.employee.lastname,
            'numss': contract.employee.num_ss ,
            'birth_date': contract.employee.birth_date ,
            'adress': contract.employee.adress,
            'type': contract.employee.type ,
            'gendre': contract.employee.gendre,
            'situation': contract.employee.situation,
            'nbr_child': contract.employee.nbr_child,
            'blood_type': contract.employee.blood_type,
            'num_carte': contract.employee.num_carte,
            'birth_address': contract.employee.birth_address ,
            'email': contract.employee.email,
            'phone': contract.employee.phone,
            'contract_type': contract.contrat_type,
            'start_date': contract.start_date,
            'end_date': contract.end_date,
            'salary_amount': contract.salary_amount,
            'status': contract.status,
            'function': contract.function,
        }

        if contract.status == "active":
            active_employees.append(employee_info)
        else:
            inactive_employees.append(employee_info)

    context = {
        'active_employees': active_employees,
        'inactive_employees': inactive_employees,
    }
    return render(request, 'HR/employee_list.html', context)



def edit_employee(request):
    if request.method == 'POST':
        employee_id = request.POST.get('id')
        employee = get_object_or_404(Employee, pk=employee_id)

        # Update all fields with data from the form
        employee.num_ss = request.POST.get('num_ss')
        employee.type = request.POST.get('type')
        employee.firstname = request.POST.get('firstname')
        employee.lastname = request.POST.get('lastname')
        employee.birth_date = request.POST.get('birth_date')  # Ensure the date format is correct
        employee.adress = request.POST.get('adress')
        employee.phone = request.POST.get('phone')
        employee.gendre = request.POST.get('gendre')
        employee.email = request.POST.get('email')
      
        employee.situation = request.POST.get('situation')
        employee.nbr_child = request.POST.get('nbr_child')
        employee.blood_type = request.POST.get('blood_type')
        employee.birth_address = request.POST.get('birth_address')
        employee.num_carte = request.POST.get('num_carte')
        employee.photo = request.POST.get('photo')

        # Save the updated employee record
        employee.save()

        # Redirect to the list of employees or another appropriate view
        return redirect('list_employee')  # Replace with your actual view name


def details(request, employee_id):
    employee = get_object_or_404(Employee, idemployee=employee_id)
    return render(request, 'HR/Details_employe.html', {'employee': employee})