from django.urls import path
from . import views

urlpatterns =[
    path('index' ,views.index ,name='index'),
    path('login' ,views.login,name='login'),
     path('signup' ,views.signup,name='signup'),
        path('add_employee/', views.add_employee, name='add_employee'),
          
         path('list_employee/', views.show_employees_contract, name='list_employee'),
       path('edit_employee/', views.edit_employee, name='edit_employee'),
     path('employee/details/<int:employee_id>/', views.details, name='employee_details'),
]