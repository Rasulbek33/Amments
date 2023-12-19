from django.shortcuts import render
from home_2.models import Home_2
from django.views.generic import ListView
from django.utils.translation import gettext as _


def home_2(request):
    home_2 = Home_2.objects.all()
    context = {'home_2':home_2}
    return render(request, 'home_2.html', context)


