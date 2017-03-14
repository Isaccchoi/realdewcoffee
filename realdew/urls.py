from django.conf import settings
from django.conf.urls import include
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
# from django.contrib.auth import views as auth_views

from main import views as main_views
from main.views import location
from main.views import DutchOrderView



urlpatterns = [
    url(r'^$', main_views.home, name='home'),
    url(r'^aboutus/$', main_views.aboutus, name='aboutus'),
    url(r'^menu/', include('menu.urls')),
    url(r'^location/$', location, name='location'),
    url(r'^order/$', DutchOrderView.as_view(), name='dutch_order'),
    # fixme need to add About Us
    # url(r'^login/$', auth_views.login, name='login'),
    # url(r'^logout/$', auth_views.logout, name='logout'),
    # url(r'^oauth/', include('social.apps.django_app.urls', namespace='social')),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
