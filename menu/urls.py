from django.conf import settings
from django.conf.urls import include
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin


from .views import MenuListView
from .views import MenuDetailView



urlpatterns = [
    url(r'^$', MenuListView.as_view(), name='menu_list'),
    url(r'^(?P<slug>\w+)/$', MenuDetailView.as_view(), name='menu_detail'),
    # 메뉴 / 핸드드립(자세히)
    # 핸드드립 주문
]
