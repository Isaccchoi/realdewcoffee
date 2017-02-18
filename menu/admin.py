from django.contrib import admin

# Register your models here.

from .models import Beverage
from .models import Category

class BeverageAdmin(admin.ModelAdmin):
    fields = ['name', 'name_eng', 'price', 'category', 'description', 'on_sale']
    models = Beverage
    list_display = ('name','price','on_sale', 'get_category')

    def get_category(self, obj):
        return obj.category.name

    def save_model(self, request, obj, form, change):
        if form.cleaned_data['slug'] == "":
            obj.slug = slugify(form.cleaned_data['name_eng'])
        obj.save()

admin.site.register(Beverage, BeverageAdmin)


class CategoryAdmin(admin.ModelAdmin):
    models = Category
    list_display = ('name',)

admin.site.register(Category, CategoryAdmin)
