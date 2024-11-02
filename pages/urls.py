from django.urls import path
from .views import rh_views

urlpatterns =[
    path('index' ,rh_views.index ,name='index'),
    path('login' ,rh_views.login,name='login'),
     path('signup' ,rh_views.signup,name='signup'),
        path('cards' ,rh_views.carde,name='cards')
]