from django.conf import settings
from django.conf.urls import include
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import login
from django.contrib.auth.views import logout

from main import views as main_views
from main.views import location
from main.views import DutchOrderView



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', main_views.home , name='home'),
    url(r'^menu/', include('menu.urls')),
    url(r'^location/$', location, name='location'),
    url(r'^order/$', DutchOrderView.as_view(), name='dutch_order'),
    url(r'', include('social.apps.django_app.urls', namespace='social')),
    url(r'^logut/$', logout, {'next_page': settings.LOGIN_URL}),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
