from django.contrib import admin

# Register your models here.
from .models import Image

from .models import User
from .models import CategoryForImage
from .models import MainImage

class ImageAdmin(admin.ModelAdmin):
    model = Image
    list_display = ('name', 'image', 'categotyimage')

admin.site.register(Image, ImageAdmin)

admin.site.register(User)

admin.site.register(CategoryForImage)

class MainImageAdmin(admin.ModelAdmin):
    fields = ('name', 'image', 'location', 'active')
    models = MainImage
    list_display = ('name', 'location', 'image')

admin.site.register(MainImage, MainImageAdmin)
