from django.conf import settings
from django.conf.urls import include
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin

from main import views as main_views



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', main_views.home , name='home'),
    # 메뉴
    # 메뉴 / 커피 및 티(자세히)
    # 메뉴 / 핸드드립(자세히)
    # 메뉴 / 디저트
    # 핸드드립 주문
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
