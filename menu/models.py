from django.db import models
from django.utils.text import slugify

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=120, null=False, blank=False, unique=True)

    def __str__(self):
        return self.name



class Beverage(models.Model):
    name = models.CharField(max_length=120, null=False, blank=False, unique=True)
    name_eng = models.CharField(max_length=120, null=False, blank=False, unique=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    price = models.PositiveIntegerField(null=False, blank=False)
    category = models.ForeignKey(Category)
    description = models.TextField()
    on_sale = models.BooleanField(default=True)
    # 이미지

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["id", "name_eng"]



class HandDrip(models.Model):
    region = models.CharField(max_length=120, null=False, blank=False)
    region_eng = models.CharField(max_length=120, null=False, blank=False)
    name = models.CharField(max_length=120, null=False, blank=False)
    name_eng = models.CharField(max_length=120,null=True, blank=True)
    description = models.TextField()
    price = models.PositiveIntegerField(null=False, blank=False)
    on_sale = models.BooleanField(default=True)
    roasting_date = models.DateTimeField()

    def __str__(self):
        return self.name


    class Meta:
        ordering = ["id", "name_eng"]
