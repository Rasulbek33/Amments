from django.urls import path
from home_1 import views

app_name = 'home_1'

urlpatterns =[
    path('home_1/', views.home_1, name='home_1'),
]