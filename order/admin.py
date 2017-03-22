from django.contrib import admin

# Register your models here.
from .models import DutchOrder
from .models import SeogyodongOrder

from datetime import datetime
from datetime import timedelta



class DutchOrderAdmin(admin.ModelAdmin):
    fields = ('user', 'reserve_at', 'quantity')
    model = DutchOrder
    list_display = ("user","created_at", 'reserve_at', 'quantity', 'total_charge')

    def save_model(self, request, obj, form, change):
        obj.total_charge = form.cleaned_data['quantity'] * 12000
        obj.reserve_at = datetime.now()+timedelta(days=30)
        obj.save

admin.site.register(DutchOrder, DutchOrderAdmin)


class SeogyodongOrderAdmin(admin.ModelAdmin):
    fields = ('user', 'reserve_at', 'quantity')
    model = SeogyodongOrder
    list_display = ("user","created_at", 'reserve_at', 'quantity', 'total_charge')

    def save_model(self, request, obj, form, change):
        obj.total_charge = form.cleaned_data['quantity'] * 4000
        obj.reserve_at = datetime.now()+timedelta(days=30)
        obj.save

admin.site.register(SeogyodongOrder, SeogyodongOrderAdmin)
