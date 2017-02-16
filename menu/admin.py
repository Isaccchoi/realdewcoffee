from django.contrib import admin

# Register your models here.

from .models import Coffee
from .models import Tea
from .models import Desert
from .models import HandDrip

class CoffeeAdmin(admin.ModelAdmin):
    models = Coffee
    list_display = ('name','price','on_sale')

admin.site.register(Coffee, CoffeeAdmin)



class TeaAdmin(admin.ModelAdmin):
    models = Tea
    list_display = ('name','price','on_sale')

admin.site.register(Tea, TeaAdmin)



class DesertAdmin(admin.ModelAdmin):
    models = Desert
    list_display = ('name','price','on_sale')

admin.site.register(Desert, DesertAdmin)


class HandDripAdmin(admin.ModelAdmin):
    models = HandDrip
    list_display = ('name','price','on_sale')

admin.site.register(HandDrip, HandDripAdmin)
