
from django.urls import path, include
from .views import *

urlpatterns = [
    path('',index,name='login_view'),
    path('signup',signupview,name='signup_view'),
    path('patienthome',patient_home,name='patient_home_view'),
    path('logout',logoutview,name='logout_view'),
    path('adddiet',add_diet,name='diet_view'),

]
