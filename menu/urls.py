from django.conf import settings
from django.conf.urls import include
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin


from .views import MenuListView
# from .views import MenuDetailView
from .views import HandDripHistoryView


urlpatterns = [
    url(r'^$', MenuListView.as_view(), name='menu_list'),
    # url(r'^(?P<slug>[\w-]+)/$', MenuDetailView.as_view(), name='menu_detail'),
    url(r'^handdrip/$', HandDripHistoryView.as_view(), name='handdrip_history'),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
