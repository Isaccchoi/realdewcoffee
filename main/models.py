from django.conf import settings
from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone

from datetime import datetime
from datetime import date
from datetime import time
from datetime import timedelta

# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='images/%Y/%m/%d', null=True, blank=True)

    def __str__(self):
        return self.name



class User(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, blank=True)
    phone_regex = RegexValidator(
                        regex="r^01([0|1|6|7|8|9]?)-([0-9]{3,4})-([0-9]{4})$")
    phone_number = models.CharField(max_length=13, validators = ['phone_regex'],
                        null=False, blank=True)

    def __str__(self):
        return self.phone_number



# def default_time():
#     timenow = datetime.today()
#
#     opentime = time(9, 0, 0, tzinfo=timezone.get_current_timezone())
#     closetime = time(21, 0, 0, tzinfo=timezone.get_current_timezone())
#     tomorrow = timenow + timedelta(days=1)
#     if timenow.time > opentime and timenow.time < closetime:
#         ordertime = datetime.combine(tomorrow, opentime)
#     else:
#         ordertime = timenow + timedelta(hours=12)
#     return ordertime

def default_time():
    now = timezone.now()
    open = now.replace(hour=9, minute=0, second=0, microsecond=0,
                            tzinfo=timezone.get_current_timezone())
    return open if open >= now else open + timedelta(days=1)


class DutchOrder(models.Model):
    user = models.ForeignKey(User)
    quantity = models.PositiveSmallIntegerField(null=False, blank=False, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    reserve_at = models.DateTimeField(default=default_time)
    total_charge = models.PositiveIntegerField(null=False, blank=False)

    def __str__(self):
        return self.user.phone_number
