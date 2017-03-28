from django.conf.urls import url
from django.contrib import admin
# from django.contrib.auth import views as auth_views

from .views import OrderView
from .views import IdentifyView
from .views import CheckOrderView
from .views import ajax_send_pin




urlpatterns = [
    # url(r'^seogyo/$', SeogyoOrderView.as_view(), name='seogyo'),
    url(r'^verify/$', ajax_send_pin, name='ajax_send_pin'),
    url(r'^identify/$', IdentifyView.as_view(), name='identify'),
    url(r'^check/$', CheckOrderView.as_view(), name="check_order"),
    url(r'^(?P<bev>[a-z]+)/$', OrderView.as_view(), name='reserve'),
]
