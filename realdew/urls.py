from django.conf import settings
from django.conf.urls import include
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin

from main import views as main_views



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', main_views.home , name='home'),
    url(r'^menu/', include('menu.urls')),
    url(r'^location/$', main_views.location, name='location'),
    # 핸드드립 주문  !!!!수정 필요

]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
