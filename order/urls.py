from django.conf.urls import url
from django.contrib import admin
# from django.contrib.auth import views as auth_views

from .views import DutchOrderView



urlpatterns = [
    url(r'^dutch/$', DutchOrderView.as_view(), name='dutch'),
]
