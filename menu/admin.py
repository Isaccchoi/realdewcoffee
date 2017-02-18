from django.contrib import admin

# Register your models here.

from .models import Beverage
from .models import Category

class BeverageAdmin(admin.ModelAdmin):
    models = Beverage
    list_display = ('name','price','on_sale', 'get_category')

    def get_category(self, obj):
        return obj.category.name

admin.site.register(Beverage, BeverageAdmin)


class CategoryAdmin(admin.ModelAdmin):
    models = Category
    list_display = ('name',)

admin.site.register(Category, CategoryAdmin)
