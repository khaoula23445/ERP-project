from django.urls import path
from .views import rh_views

urlpatterns = [
    path('index/', rh_views.index, name='index'),
    path('login/', rh_views.login, name='login'),
    path('signup/', rh_views.signup, name='signup'),
    path('delete_employee/<int:employee_id>/', rh_views.delete_employee, name='delete_employee'),
    path('add_employee/', rh_views.add_employee, name='add_employee'),
    path('list_employee/', rh_views.show_employees_contract, name='list_employee'),
    path('edit_employee/', rh_views.edit_employee, name='edit_employee'),
    path('employee/details/<int:employee_id>/', rh_views.details, name='employee_details'),
       path('assign-project/',rh_views.assign_project, name='assign_project'),
      path('change_status_to_inactive/<int:employee_id>/', rh_views.change_status_to_inactive, name='change_status_to_inactive'),
         path('contracts/', rh_views.contract_list, name='contract_list'),
    path('update_contract/<int:contract_id>/', rh_views.update_contract, name='update_contract'),
    path('delete_contract/<int:contract_id>/', rh_views.delete_contract, name='delete_contract'),
      path('view_contract/<int:contract_id>/', rh_views.view_contract, name='view_contract'), 
    path('conges/', rh_views.list_conges, name='list_conges'),
   path('add_conge/', rh_views.add_conge, name='add_conge'),
  path('update-conge/', rh_views.update_conge, name='update-conge'),
    path('delete_conge/', rh_views.delete_conge, name='delete_conge'),
     path('attendance/', rh_views.attendance_view, name='attendance_view'),
  path('salary_list/',rh_views.salary_list, name='salary_list'),
     path('payroll_list/', rh_views.payroll_list, name='payroll_list'),
       path('payroll/delete/<int:payroll_id>/', rh_views.delete_payroll, name='delete_payroll'),
    path('generate_payslip/<int:payroll_id>/', rh_views.generate_payslip, name='generate_payslip'),
   path('payroll/details/<int:payroll_id>/', rh_views.get_payroll_details, name='get_payroll_details'),

 path('payroll/update/<int:payroll_id>/', rh_views.update_payroll, name='update_payroll'),
]
