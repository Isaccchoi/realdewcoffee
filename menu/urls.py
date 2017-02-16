from django.conf import settings
from django.conf.urls import include
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin


from .views import MenuListView



urlpatterns = [
    url(r'^$', MenuListView.as_view(), name='menu')
    # 메뉴 / 커피 및 티(자세히)
    # 메뉴 / 핸드드립(자세히)
    # 메뉴 / 디저트
    # 핸드드립 주문
]
