

from datetime import date, timedelta
from pyexpat.errors import messages
import traceback
from django.shortcuts import get_object_or_404, redirect, render
from django.http import Http404, HttpResponse, JsonResponse
from django.urls import reverse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from pages.models import Employee, Contrat, Conge, Contrat, EmployeePayment,EmployeeProject,Pointage,ReviewEmployer,Salary,Admin,Secretary,Project,Users,Salary, Payrolls, Pointage,Caisse,CaisseTransaction ,BankAccount, BankTransaction
from django.db import transaction
from django.views.decorators.http import require_http_methods
from django.db import models
from decimal import Decimal
import pdfkit
from django.http import HttpResponse
from django.template.loader import render_to_string
import json
from datetime import datetime, date, timedelta
from django.template import loader

from django.utils.timezone import now

def login(request):
    return render(request,'pages/signin.html')
def signup(request):
    return render(request,'pages/signup.html')
def index(request):
    return render(request,'pages/index.html')


def add_employee(request):
    if request.method == "POST":
        with transaction.atomic():
            
              
            user = Users(

                        username=request.POST.get('username'),
                        password=request.POST.get('password'),
                        user_type=request.POST.get('user_type'),
                    )
            user.save()

          
            employee = Employee(
                num_ss=request.POST.get('num_ss'),
                type=request.POST.get('type'),
                iduser =user,
                phone=request.POST.get('phone'),
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
                role=request.POST.get('role'),
                departement=request.POST.get('departement')
            )
            employee.save()

           
            contract = Contrat(
                contrat_type=request.POST.get('contrat_type'),
                start_date=request.POST.get('start_date'),
                end_date=request.POST.get('end_date'),
                salary_amount=request.POST.get('salary_amount'),
                status=request.POST.get('status'),
                job_title=request.POST.get('job_title'),
                employee=employee,
                contrat_terms=request.POST.get('contrat_terms'),
                work_location=request.POST.get('work_location'),
                work_hours= request.POST.get('work_hours'),
                created_at= request.POST.get('created_at'),
            )
            contract.save()

        return render(request, 'HR/add_employee.html')

    return render(request, 'HR/add_employee.html')

def show_employees_contract(request):
    
    contracts = Contrat.objects.select_related('employee').all()
    projects = Project.objects.all()
    active_employees = []
    inactive_employees = []

    for contract in contracts:
        employee_info = {
            'id': contract.employee.idemployee,
            'firstname': contract.employee.firstname,
            'lastname': contract.employee.lastname,
            'numss': contract.employee.num_ss,  # Updated field
            'birth_date': contract.employee.birth_date,
            'birth_address': contract.employee.birth_address,
            'adress': contract.employee.adress,
            'phone': contract.employee.phone,
            'email': contract.employee.email,
            'type': contract.employee.type,
            'gendre': contract.employee.gendre,
            'situation': contract.employee.situation,
            'nbr_child': contract.employee.nbr_child,
            'blood_type': contract.employee.blood_type,
            'num_carte': contract.employee.num_carte,
            'role': contract.employee.role,
            'departement': contract.employee.departement,
            'contract_type': contract.contrat_type,
            'start_date': contract.start_date,
            'end_date': contract.end_date,
            'salary_amount': contract.salary_amount,
            'status': contract.status,
            'job_title': contract.job_title,  
            'work_location': contract.work_location, 
            'work_hours': contract.work_hours,  
        }

        if contract.status == "Active":
            active_employees.append(employee_info)
        else:
            inactive_employees.append(employee_info)

    context = {
        'active_employees': active_employees,
        'inactive_employees': inactive_employees,
        'projects': projects
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
        employee.birth_date = request.POST.get('birth_date') 
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
        employee.departement = request.POST.get('departement')
     
        employee.save()

        
        return redirect('list_employee')  


def details(request, employee_id):
    employee = get_object_or_404(Employee, idemployee=employee_id)
    return render(request, 'HR/Details_employe.html', {'employee': employee})



@csrf_exempt
@require_http_methods(["DELETE"])
def delete_employee(request, employee_id):
   
        # Retrieve the employee object or return 404 if not found
        employee = get_object_or_404(Employee,  idemployee=employee_id)

        # Delete related records in other tables
        Conge.objects.filter(employee=employee).delete()
        Contrat.objects.filter(employee=employee).delete()
        EmployeePayment.objects.filter(employee=employee).delete()
        EmployeeProject.objects.filter(employee=employee).delete()
        Pointage.objects.filter(employee_id=employee).delete()
        ReviewEmployer.objects.filter(employee=employee).delete()
        Salary.objects.filter(employee=employee).delete()
        Admin.objects.filter(employee=employee).delete()
        Secretary.objects.filter(employee=employee).delete()
        
        # Delete the employee
        employee.delete()

        return JsonResponse({'success': True})


def change_status_to_inactive(request, employee_id):
    if request.method == "POST":
        try:
            contract = Contrat.objects.get(employee_id=employee_id)
            contract.status = "inactive"
            contract.end_date = timezone.now() 
            contract.save()
            return JsonResponse({"success": True})
        except Contrat.DoesNotExist:
            return JsonResponse({"success": False, "error": "Contract not found"}, status=404)
    return JsonResponse({"success": False, "error": "Invalid request"}, status=400)


def assign_project(request):
    if request.method == 'POST':
        employee_id = request.POST.get('employee_id')
        project_id = request.POST.get('project')  # This now retrieves the project ID from the dropdown
        role = request.POST.get('role')
        assigned_date = request.POST.get('assigned_date', timezone.now().date())
        projects = Project.objects.all()
        # Get Employee and Project instances
        employee = get_object_or_404(Employee, idemployee=employee_id)
        project = get_object_or_404(Project, project_id=project_id)
        employees = Employee.objects.all()
        projects = Project.objects.all()  #
        # Save the project assignment in EmployeeProject model
        assignment = EmployeeProject.objects.create(
            employee=employee,
            project=project,
            role=role,
            assigned_date=assigned_date
        )

        
        return redirect(reverse('list_employee'))  # Adjust redirect to your employee listing URL

    
    return render(request, 'HR/employee_list.html', {'employees': employees, 'projects': projects})

def contract_list(request):
    contracts = Contrat.objects.all()
    return render(request, ' contract_list.html', {'contracts': contracts})



def contract_list(request):
    contracts = Contrat.objects.select_related('employee').all() 
    return render(request, 'HR/contrat_list.html', {'contracts': contracts})


def update_contract(request, contract_id):
    if request.method == 'POST':
        contract = get_object_or_404(Contrat, pk=contract_id)
        contract.status = request.POST.get('status')
        contract.end_date = request.POST.get('end_date', timezone.now())
        contract.salary_amount = request.POST.get('salary_amount')
        contract.work_location= request.POST.get('work_location')
        contract.start_date = request.POST.get('start_date')
        contract.contrat_type = request.POST.get('type')
        contract.job_title = request.POST.get('function')
        contract.work_hours = request.POST.get('work_hours')  
        contract.created_at=request.POST.get('created')  
        contract.save()
        return JsonResponse({"success": True})

def delete_contract(request, contract_id):
    if request.method == 'POST':
        contract = get_object_or_404(Contrat, pk=contract_id)
        contract.delete()
        return JsonResponse({"success": True})


def view_contract(request, contract_id):
    contract = get_object_or_404(Contrat, pk=contract_id)
    
    # Load the template
    template = loader.get_template('HR/contract_pdf.html')
    context = {'contract': contract}
    html = template.render(context)

    # Generate PDF
    pdf_file = pdfkit.from_string(html, False)  # Generate PDF from HTML string

    # Create the response
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="contract_{contract.idcontrat}.pdf"'
    return response


def check_conges():
    
    today = datetime.today().date()

    conges = Conge.objects.filter(
        status__in=['approuvé', 'en cours'],  
    )

    for conge in conges:
    
        if conge.start_date and conge.end_date:
            
            if conge.start_date <= today <= conge.end_date:
                if conge.status != 'en cours':  
                    conge.status = 'en cours'
                    conge.save()

            elif today > conge.end_date:
                if conge.status != 'terminé':  
                    conge.status = 'terminé'
                    conge.save()
        else:
            print(f"Les dates du congé  sont invalides ou manquantes.")
    
    return "Vérification des congés terminée."

def list_conges(request):
    check_conges()
    employee = Employee.objects.all()
    conges = Conge.objects.select_related('employee').all()


    return render(request, 'HR/list_conges.html', {'conges': conges ,'employee':employee})


def add_conge(request):
    if request.method == 'POST':
        employee_id = request.POST.get('employee_id')
        conge_type = request.POST.get('conge_type')
        start_date = request.POST.get('start_date')
        num_days = int(request.POST.get('num_days'))

        try:
         
            employee = Employee.objects.get(idemployee=employee_id)

            
            start_date = date.fromisoformat(start_date)

            end_date = start_date + timedelta(days=num_days - 1)
            overlapping_conge = Conge.objects.filter(
                employee=employee,
                status__in=['en cours', 'approuvé'],  
                start_date__lte=end_date,
                end_date__gte=start_date
            )

            if overlapping_conge.exists():
                return JsonResponse({
                    'status': 'error',
                    'message': "L'employé est déjà en congé pendant cette période."
                })

            conges_payes = Conge.objects.filter(employee=employee, conge_type='Payé', status__in=['approuvé', 'en cours'])
            total_days_taken = sum([conge.num_days for conge in conges_payes])

            
            remaining_days = 30 - total_days_taken

            if remaining_days < num_days:
                return JsonResponse({
                    'status': 'error',
                    'message': f"Jours de congés payés insuffisants. Restants : {remaining_days}."
                })

            num_days_rest = remaining_days - num_days

            conge = Conge.objects.create(
                employee=employee,
                conge_type=conge_type,
                start_date=start_date,
                end_date=end_date,
                num_days=num_days,
                num_days_rest=num_days_rest,
                status='approuvé'  # Statut par défaut à approuvé
            )

            # Mise à jour automatique du statut du congé
            today = date.today()
            if conge.start_date <= today <= conge.end_date:
                conge.status = 'en cours'  # Si le congé est en cours, mettre à 'en cours'
            elif today > conge.end_date:
                conge.status = 'terminé'  # Si le congé est passé, mettre à 'terminé'
            conge.save()

            # Retourner une réponse JSON avec succès
            return JsonResponse({'status': 'success', 'message': "Le congé a été ajouté avec succès."})

        except Employee.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': "L'employé spécifié n'existe pas."})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': f"Une erreur est survenue : {str(e)}"})

    return JsonResponse({'status': 'error', 'message': "Requête non valide."})


def update_conge(request):
    if request.method == 'POST':
        conge_id = request.POST.get('idconge')  
        employee_id = request.POST.get('employee')  
        conge_type = request.POST.get('conge_type')  
        start_date = request.POST.get('start_date')  
        num_days = request.POST.get('num_days')  
        status = request.POST.get('status')  
        from datetime import timedelta, datetime

        if start_date:
            start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
            end_date = start_date + timedelta(days=int(num_days))
        else:
            end_date = None

        conge = get_object_or_404(Conge, idconge=conge_id)

        conge.employee_id = employee_id
        conge.conge_type = conge_type
        conge.start_date = start_date
        conge.end_date = end_date
        conge.num_days = num_days
        conge.status = status
        conge.save()

       
        return JsonResponse({'success': True, 'message': 'Congé updated successfully!'})

    return JsonResponse({'success': False, 'message': 'Invalid request method.'})


def update_conge(request, idconge):
    conge = get_object_or_404(Conge, idconge=idconge)

    if request.method == "GET":
       
        return JsonResponse({
            "idconge": conge.idconge,
            "employee_id": conge.employee.idemployee,
            "conge_type": conge.conge_type,
            "start_date": conge.start_date,
            "num_days": conge.num_days,
            "end_date": conge.end_date
        })

    elif request.method == "POST":
       
        data = json.loads(request.body)
        try:
            employee = Employee.objects.get(idemployee=data["employee_id"])
            conge.employee = employee
            conge.conge_type = data["conge_type"]
            conge.start_date = data["start_date"]
            conge.num_days = int(data["num_days"])
            conge.end_date = data["end_date"]
            conge.save()
            return JsonResponse({"success": True})
        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)})

    return JsonResponse({"success": False, "error": "Invalid request method."})


def delete_conge(request):
    if request.method == 'POST':
        conge_id = request.POST.get('conge_id')

        try:
            conge = get_object_or_404(Conge, idconge=conge_id)
            conge.delete()

            return JsonResponse({'status': 'success', 'message': "Le congé a été supprimé avec succès."})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': f"Une erreur est survenue : {str(e)}"})

    return JsonResponse({'status': 'error', 'message': "Requête non valide."})

def initialize_daily_attendance():
    today = timezone.now().date()
    employees = Employee.objects.all()
    for employee in employees:
        Pointage.objects.get_or_create(
            date=today,
            employee_id=employee,
            defaults={'status': 'non-pointed'}
        )
from datetime import datetime, timedelta
from django.utils.timezone import make_aware

def attendance_view(request):

    initialize_daily_attendance()

    today = timezone.now().date()
    non_pointed_employees = Pointage.objects.filter(date=today, status='non-pointed')
    pointed_employees = Pointage.objects.filter(date=today).exclude(status='non-pointed')


    present_count = Pointage.objects.filter(date=today, status='present').count()
    absent_count = Pointage.objects.filter(date=today, status='absent').count()
    non_pointed_count = Pointage.objects.filter(date=today, status='non-pointed').count()
    if request.method == 'POST':
        pointage_id = request.POST.get('pointage_id')
        status = request.POST.get('status')
        overtime_hours = request.POST.get('overtime_hours') or 0  
        pointage = Pointage.objects.get(idpointage=pointage_id)

        if status == 'present':
            check_in_time = request.POST.get('check_in_time')
            check_out_time = request.POST.get('check_out_time')

            if not check_in_time or not check_out_time:
                messages.error(request, "Check-in and check-out times are required for present employees.")
                return redirect('attendance_view')

            check_in_time = make_aware(datetime.strptime(check_in_time, '%H:%M'))
            check_out_time = make_aware(datetime.strptime(check_out_time, '%H:%M'))

            total_hours = (check_out_time - check_in_time).total_seconds() / 3600  # Convert to hours
            pointage.total_hours_worked = round(total_hours, 2)

            pointage.overtime_hours = round(float(overtime_hours), 2)

            pointage.status = 'present'
            pointage.check_in_time = check_in_time.time()
            pointage.check_out_time = check_out_time.time()
        elif status == 'absent':
            pointage.status = 'absent'
            pointage.check_in_time = None
            pointage.check_out_time = None
            pointage.total_hours_worked = 0
            pointage.overtime_hours = 0

        pointage.save()
        return redirect('attendance_view')

    return render(request, 'HR/attendance.html', {
        'non_pointed_employees': non_pointed_employees,
        'pointed_employees': pointed_employees,
        'present_count': present_count,
        'absent_count': absent_count,
        'non_pointed_count': non_pointed_count,
    })

def attendance_history(request):
    year = request.GET.get('year')
    month = request.GET.get('month')
    day = request.GET.get('day')
    history_records = Pointage.objects.all()

    if year:
        history_records = history_records.filter(date__year=year)
    if month:
        history_records = history_records.filter(date__month=month)
    if day:
        history_records = history_records.filter(date=day)

    context = {
        'history_records': history_records,
    }
    return render(request, 'HR/attendance_history.html', context)

def salary_list(request):
    salaries = Salary.objects.all()  
    employees = Employee.objects.all()  
    return render(request, 'HR/salary_list.html', {'salaries': salaries, 'employees': employees})
def payroll_list(request):
    if request.method == "POST":
        employee_id = request.POST.get('employee')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        bonus = Decimal(request.POST.get('bonus', '0'))
        overtime_rate = Decimal(request.POST.get('overtime_rate', '0'))
        hourly_rate = Decimal(request.POST.get('hourly_rate', '0'))
        daily_deduction_rate = Decimal(request.POST.get('deduction_rate', '0'))
        payment_method = request.POST.get('payment_method')
        payment_account_id = request.POST.get('payment_account_id')  
        cheque_number = request.POST.get('cheque_number')  

        if not all([employee_id, start_date, end_date, payment_method, payment_account_id]):
            messages.error(request, "All fields are required, including payment details.")
            return redirect('payroll_list')

        try:
     
            employee = Employee.objects.get(idemployee=employee_id)
            pointage_records = Pointage.objects.filter(
                employee_id=employee, date__range=[start_date, end_date]
            )

            total_regular_hours = sum(
                Decimal(record.total_hours_worked or 0) for record in pointage_records
            )
            total_overtime_hours = sum(
                Decimal(record.overtime_hours or 0) for record in pointage_records
            )
            total_absent_days = sum(
                1 for record in pointage_records if not record.total_hours_worked
            )

           
            monthly_work_hours = Decimal(160)
            base_salary = hourly_rate * monthly_work_hours
            overtime_pay = total_overtime_hours * overtime_rate
            absence_deduction = total_absent_days * daily_deduction_rate
            net_amount = base_salary + overtime_pay + bonus - absence_deduction
            start_time = None
            end_time = None
            if pointage_records:
                first_record = pointage_records.first()
                last_record = pointage_records.last()

                
                if first_record.check_in_time:
                    start_time = first_record.check_in_time

                if last_record.check_out_time:
                    end_time = last_record.check_out_time
         
            with transaction.atomic():
                if payment_method == "Caisse":
                    caisse = Caisse.objects.get(caisse_id=payment_account_id)
                    if caisse.current_balance < net_amount:
                        raise ValueError("Insufficient balance in Caisse.")
                    caisse.current_balance -= net_amount
                    
                    caisse.save()
                    CaisseTransaction.objects.create(
                        caisse=caisse,
                        transaction_date=now(),
                        amount=net_amount,
                        transaction_type="Expense",
                        designation=f"Payroll for {employee.firstname} {employee.lastname}",
                        payer_type="Client",

                    )
                elif payment_method == "Bank":
                    bank_account = BankAccount.objects.get(bank_account_id=payment_account_id)
                    if bank_account.real_balance < net_amount:
                        raise ValueError("Insufficient balance in Bank Account.")
                    bank_account.real_balance -= net_amount
                     #bank_account.updated_at=now() 
                    bank_account.save()
                    BankTransaction.objects.create(
                        bank_account=bank_account,
                        transaction_date=now(),
                        amount=net_amount,
                        transaction_type="Expense",
                        cheque_number=cheque_number,  # Store the cheque number
                        payer_type="Client",
                      
                        pay_method='Cheque'
                    )

                # Record payroll
                Payrolls.objects.create(
                    employee=employee,
                    pay_date=now(),
                   
                    pay_period_start=start_date,
                    pay_period_end=end_date,
                    total_amount=net_amount,
                    regular_pay=base_salary,
                    overtime_pay=overtime_pay,
                    deductions=absence_deduction,
                    bonuses=bonus,
                    payroll_status="Paid",
                    net_pay=net_amount,
                    start_time=start_time,
                    end_time=end_time,
                    overtime_rate=overtime_rate,
                    hourly_rate=hourly_rate,
                     total_hours_work= None  , #should ask snds
           
                    overtime_hours= Decimal( total_overtime_hours ), 
           
                 
                )

            messages.success(request, f"Payroll processed successfully for {employee.firstname} {employee.lastname}.")
        except Employee.DoesNotExist:
            messages.error(request, "Selected employee does not exist.")
        except ValueError as e:
            messages.error(request, str(e))
        except Exception as e:
            messages.error(request, f"An unexpected error occurred: {e}")
        return redirect('payroll_list')

    payrolls = Payrolls.objects.all()
    employees = Employee.objects.all()
    caisses = Caisse.objects.all()
    bank_accounts = BankAccount.objects.all()

    return render(request, 'HR/payroll_list.html', {
        'payrolls': payrolls,
        'employees': employees,
        'caisses': caisses,
        'bank_accounts': bank_accounts,
    })


def generate_payslip(request, payroll_id):
    try:
     
        payroll = Payrolls.objects.get(payroll_id=payroll_id)

        context = {
            'payroll': payroll,
            'employee': payroll.employee,
        }
        html = render_to_string('HR/payslip_template.html', context)
        pdf = pdfkit.from_string(html, False)
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = f'inline; filename="payslip_{payroll.employee.firstname}_{payroll.pay_date}.pdf"'

        return response
    except Payrolls.DoesNotExist:
        return HttpResponse("Payroll not found", status=404)


def delete_payroll(request, payroll_id):
    payroll = get_object_or_404(Payrolls, payroll_id=payroll_id)

    try:
        payroll.delete()
        messages.success(request, "Payroll entry deleted successfully.")
    except Exception as e:
        messages.error(request, f"Error deleting payroll entry: {e}")

    return redirect('payroll_list')  # Redirect to the payroll list page after deletion


def get_payroll_details(request, payroll_id):
    try:
        payroll = Payrolls.objects.get(payroll_id=payroll_id)
        data = {
            'employee_name': f"{payroll.employee.firstname} {payroll.employee.lastname}",
            'start_date': payroll.pay_period_start,
            'end_date': payroll.pay_period_end,
            'bonus': payroll.bonuses,
            'hourly_rate': payroll.regular_pay / Decimal(160),  # Assume 160 monthly work hours
            'overtime_rate': payroll.overtime_pay ,
            'deduction_rate': payroll.deductions ,

        }
        return JsonResponse(data)
    except Payrolls.DoesNotExist:
        return JsonResponse({'error': 'Payroll not found'}, status=404)



def update_payroll(request, payroll_id):
    try:
        payroll = get_object_or_404(Payrolls, payroll_id=payroll_id)

        if request.method == 'POST':
            start_date = request.POST.get('start_date')
            end_date = request.POST.get('end_date')
            bonus = Decimal(request.POST.get('bonus', '0'))
            overtime_rate = Decimal(request.POST.get('overtime_rate', '0'))
            hourly_rate = Decimal(request.POST.get('hourly_rate', '0'))
            deduction_rate = Decimal(request.POST.get('deduction_rate', '0'))
            payment_method = request.POST.get('payment_method')
            payment_account_id = request.POST.get('payment_account_id')
            cheque_number = request.POST.get('cheque_number', '')

            # Update payroll fields
            payroll.pay_period_start = start_date
            payroll.pay_period_end = end_date
            payroll.bonuses = bonus
            payroll.regular_pay = hourly_rate * 160  # Example calculation
            payroll.overtime_pay = overtime_rate
            payroll.deductions = deduction_rate
            payroll.payment_method = payment_method
            payroll.payment_account_id = payment_account_id
            payroll.cheque_number = cheque_number
            payroll.total_amount = payroll.regular_pay + payroll.overtime_pay + payroll.bonuses - payroll.deductions
            payroll.payroll_status = "Paid"

            payroll.save()

            messages.success(request, "Payroll updated successfully.")
            return redirect('payroll_list')  # Redirect to payroll list or another page

    except Exception as e:
        messages.error(request, f"An error occurred: {e}")
        return redirect('payroll_list')
