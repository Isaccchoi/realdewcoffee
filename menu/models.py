from django.db import models

# Create your models here.

class Beverage(models.Model):
    name = models.CharField(max_length=120, null=False, blank=False)
    price = models.PositiveIntegerField(null=False, blank=False)
    description = models.TextField()
    on_sale = models.BooleanField(default=True)
    #이미지

class HandDrip(models.Model):
    region = models.CharField(max_length=120, null=False, blank=False)
    name = models.CharField(max_length=120, null=False, blank=False)
    description = models.TextField()
    price = models.PositiveIntegerField(null=False, blank=False)
    on_sale = models.BooleanField(default=True)
    roasting_date = models.DateTimeField()
    # 이미지?
