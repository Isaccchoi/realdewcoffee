
from django.contrib import admin
from django.utils import timezone
from django.utils.text import slugify

# Register your models here.

from .models import Beverage
from .models import Category
from .models import HandDrip
from .models import Desert

class BeverageAdmin(admin.ModelAdmin):
    fields = ['name', 'name_eng', 'price', 'category', 'on_sale', 'hot','warm', 'ice']
    models = Beverage
    list_display = ('name','price','on_sale', 'category', 'slug')
    list_filter = (('category', admin.RelatedOnlyFieldListFilter),)

    def save_model(self, request, obj, form, change):
        obj.slug = slugify(form.cleaned_data['name_eng'])
        if obj.hot == True and obj.warm == True:
            obj.warm = False
        obj.save()

admin.site.register(Beverage, BeverageAdmin)


class CategoryAdmin(admin.ModelAdmin):
    models = Category
    list_display = ('name',)

admin.site.register(Category, CategoryAdmin)


class HandDripAdmin(admin.ModelAdmin):
    fields = ['region', 'name', 'region_eng', 'name_eng', 'price', 'on_sale', 'roasting_date',]
    models = HandDrip
    list_display = ('region', 'name', 'region_eng', 'name_eng', 'price', 'on_sale', 'roasting_date', 'start_sale_date', 'end_sale_date',)
    list_filter = ('on_sale',)

    def save_model(self, request, obj, form, change):
        obj.slug = slugify(form.cleaned_data['name_eng']) + slugify(form.cleaned_data['region_eng']) + '-' + slugify(form.cleaned_data['roasting_date'])
        if not obj.start_sale_date:
            obj.start_sale_date = timezone.now()
        if obj.on_sale == False:
            obj.end_sale_date = timezone.now()
        obj.save()

admin.site.register(HandDrip, HandDripAdmin)


class DesertAdmin(admin.ModelAdmin):
    fields = ['name', 'name_eng', 'price', 'category', 'on_sale', 'image']
    models = Desert
    list_display = ('name', 'price', 'on_sale', 'slug')

    def save_model(self, request, obj, form, change):
        obj.slug = slugify(form.cleaned_data['name_eng'])
        obj.save()

admin.site.register(Desert, DesertAdmin)
