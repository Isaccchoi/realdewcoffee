from django.contrib import admin

# Register your models here.
from .models import Order
from .models import Beverage
# from .models import SeogyodongOrder

from datetime import datetime
from datetime import timedelta



class OrderAdmin(admin.ModelAdmin):
    fields = ('user', 'reserve_at', 'quantity')
    model = Order
    list_display = ("user","created_at", 'reserve_at', 'quantity', 'total_charge')

    def save_model(self, request, obj, form, change):
        obj.total_charge = form.cleaned_data['quantity'] * 12000
        obj.reserve_at = datetime.now()+timedelta(days=30)
        obj.save

admin.site.register(Order, OrderAdmin)


class BeverageAdmin(admin.ModelAdmin):
    field = ("name", "price","image")
    model = Beverage
    list_display = ("name", "price")

admin.site.register(Beverage, BeverageAdmin)
#
# class SeogyodongOrderAdmin(admin.ModelAdmin):
#     fields = ('user', 'reserve_at', 'quantity')
#     model = SeogyodongOrder
#     list_display = ("user","created_at", 'reserve_at', 'quantity', 'total_charge')
#
#     def save_model(self, request, obj, form, change):
#         obj.total_charge = form.cleaned_data['quantity'] * 4000
#         obj.reserve_at = datetime.now()+timedelta(days=30)
#         obj.save
#
# admin.site.register(SeogyodongOrder, SeogyodongOrderAdmin)
