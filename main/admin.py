from django.contrib import admin

# Register your models here.
from .models import Image
from .models import DutchOrder
from .models import User
from .models import CategoryForImage
from .models import MainImage

class ImageAdmin(admin.ModelAdmin):
    model = Image
    list_display = ('name', 'image', 'categotyimage')

admin.site.register(Image, ImageAdmin)


class DutchOrderAdmin(admin.ModelAdmin):
    fields = ('user','reserve_at')
    model = DutchOrder
    list_display = ("user","created_at", 'reserve_at', 'quantity', 'total_charge')

    def save_model(self, request, obj, form, change):
        obj.total_charge = form.cleaned_data['quantity'] * 12000
        obj.reserve_at = datetime.now()+timedelta(days=30)
        obj.save

admin.site.register(DutchOrder, DutchOrderAdmin)


admin.site.register(User)

admin.site.register(CategoryForImage)

class MainImageAdmin(admin.ModelAdmin):
    fields = ('name', 'image', 'location', 'active')
    models = MainImage
    list_display = ('name', 'location')

admin.site.register(MainImage, MainImageAdmin)
