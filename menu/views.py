from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# Create your views here

from .models import Coffee


class MenuListView(ListView):
    model = Coffee
    queryset = Coffee.objects.all()
