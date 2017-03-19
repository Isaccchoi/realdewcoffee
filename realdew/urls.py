from django.conf import settings
from django.conf.urls import include
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
# from django.contrib.auth import views as auth_views

from main import views as main_views
from main.views import location
from main.views import DutchOrderView
from main.views import ajax_send_pin



urlpatterns = [
    url(r'^$', main_views.home, name='home'),
    url(r'^aboutus/$', main_views.aboutus, name='aboutus'),
    url(r'^menu/', include('menu.urls')),
    url(r'^location/$', location, name='location'),
    url(r'^order/$', DutchOrderView.as_view(), name='dutch_order'),
    url(r'^oder/verify/$', ajax_send_pin, name='ajax_send_pin'),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
