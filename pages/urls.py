from django.urls import path
from .views import rh_views

urlpatterns =[
    path('index' ,rh_views.index ,name='index'),
    path('login' ,rh_views.login,name='login'),
     path('signup' ,rh_views.signup,name='signup'),
    path('cards' ,rh_views.carde,name='cards')

    path('add_employee/', rh_views.add_employee, name='add_employee'),
          
        path('list_employee/', rh_views.show_employees_contract, name='list_employee'),
       path('edit_employee/', rh_views.edit_employee, name='edit_employee'),
     path('employee/details/<int:employee_id>/', rh_views.details, name='employee_details'),
   
]