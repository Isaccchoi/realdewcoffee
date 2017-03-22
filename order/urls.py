from django.conf.urls import url
from django.contrib import admin
# from django.contrib.auth import views as auth_views

from .views import DutchOrderView
from .views import SeogyoOrderView




urlpatterns = [
    url(r'^dutch/$', DutchOrderView.as_view(), name='dutch'),
    url(r'^seogyo/$', SeogyoOrderView.as_view(), name='seogyo'),
]
