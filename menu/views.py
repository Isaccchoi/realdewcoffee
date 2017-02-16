from django.shortcuts import render
from django.views.generic.list import ListView

# Create your views here

from .models import Coffee


class MenuListView(ListView):
    model = Coffee
    queryset = Coffee.objects.all()
