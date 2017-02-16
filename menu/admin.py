from django.contrib import admin

# Register your models here.

from .models import Beverage
from .models import HandDrip

admin.site.register(Beverage)

admin.site.register(HandDrip)
