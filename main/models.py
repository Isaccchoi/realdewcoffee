from django.conf import settings
from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone

from datetime import datetime
from datetime import date
from datetime import time
from datetime import timedelta

# Create your models here.
class CategoryForImage(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name



class Image(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='images/%Y/%m/%d', null=True, blank=True)
    categotyimage = models.ForeignKey(CategoryForImage, null=True)

    def __str__(self):
        return self.name



class MainImage(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/%Y/%m/%d', null=True, blank=True)
    active = models.BooleanField(default=True)
    location = models.CharField(max_length=50, null=True, blank=True)

    def __str(self):
        return self.name



class User(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, blank=True)
    phone_regex = RegexValidator(
                        regex="r^01([0|1|6|7|8|9]?[0-9]{7,8})$")
    phone_number = models.CharField(max_length=13, validators = ['phone_regex'],
                        null=False, blank=True)

    def __str__(self):
        return self.phone_number



def default_time():
    now = timezone.now()
    open = now.replace(hour=9, minute=0, second=0, microsecond=0,
                            tzinfo=timezone.get_current_timezone())
    return open if open >= now else open + timedelta(days=1)



class DutchOrder(models.Model):
    user = models.ForeignKey(User)
    quantity = models.PositiveSmallIntegerField(null=False, blank=False, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    reserve_at = models.DateTimeField(null=False, blank=True)
    total_charge = models.PositiveIntegerField(null=False, blank=False)
    email = models.EmailField(null=True, blank=False)

    def __str__(self):
        return self.user.phone_number

    class Meta:
        ordering = ['-created_at', '-id']
