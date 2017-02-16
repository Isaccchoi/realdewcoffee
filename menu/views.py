from django.shortcuts import render
from django.views.generic.list import ListView

# Create your views here

from .models import Beverage


class MenuListView(ListView):
    model = Beverage
    queryset = Beverage.objects.all()
