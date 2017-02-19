from django.contrib import admin

# Register your models here.
from .models import Image

class ImageAdmin(admin.ModelAdmin):
    model = Image
    list_display = ('name', 'image')



admin.site.register(Image, ImageAdmin)
