from django.contrib import admin

# Register your models here.
from .models import Image
from .models import DutchOrder

class ImageAdmin(admin.ModelAdmin):
    model = Image
    list_display = ('name', 'image')

admin.site.register(Image, ImageAdmin)


class DutchOrderAdmin(admin.ModelAdmin):
    fields = ['user','reserve_at', ]
    model = DutchOrder
    list_display = ("phone_regex", "created_at",
                    'reserve_at', 'quantity', 'total_charge')

    def save_model(self, request, obj, form, change):
        obj.total_charge = form.cleaned_data['quantity'] * 12000
        obj.reserve_at = datetime.now()+timedelta(days=30)
        obj.save
