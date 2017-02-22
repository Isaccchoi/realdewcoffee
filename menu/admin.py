from django.contrib import admin
from django.utils.text import slugify

# Register your models here.

from .models import Beverage
from .models import Category
from .models import HandDrip
from .models import Desert

class BeverageAdmin(admin.ModelAdmin):
    fields = ['name', 'name_eng', 'price', 'category', 'on_sale', 'hot', 'ice']
    models = Beverage
    list_display = ('name','price','on_sale', 'category', 'slug')
    list_filter = (('category', admin.RelatedOnlyFieldListFilter),)

    def save_model(self, request, obj, form, change):
        obj.slug = slugify(form.cleaned_data['name_eng'])
        obj.save()

admin.site.register(Beverage, BeverageAdmin)


class CategoryAdmin(admin.ModelAdmin):
    models = Category
    list_display = ('name',)

admin.site.register(Category, CategoryAdmin)


class HandDripAdmin(admin.ModelAdmin):
    fields = ['name', 'name_eng', 'region', 'region_eng', 'price', 'on_sale', 'roasting_date',]
    models = HandDrip
    list_display = ('name', 'name_eng', 'region', 'region_eng', 'price', 'on_sale', 'roasting_date', 'slug',)
    list_filter = ('on_sale',)

    def save_model(self, request, obj, form, change):
        obj.slug = slugify(form.cleaned_data['name_eng']) + slugify(form.cleaned_data['region_eng']) + '-' + slugify(form.cleaned_data['roasting_date'])
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
