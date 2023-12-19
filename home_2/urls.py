from django.urls import path
from home_2 import views


app_name = 'home_2'



urlpatterns = [
    path('home_2/', views.home_2, name='home_2'),

]

