from django.shortcuts import render
from home_1.models import Home_1

def home_1(request):
    home_1 = Home_1.objects.all()
    context = {'home1':home_1}
    return render(request, 'home_1.html', context)


