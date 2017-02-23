from django.core.validators import RegexValidator
from django.db import models
from django.urls import reverse


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
    hot = models.BooleanField(default=True)
    warm = models.BooleanField(default=False)
    ice = models.BooleanField(default=True)
    category = models.ForeignKey(Category)
    description = models.TextField(null=True, blank=True)
    on_sale = models.BooleanField(default=True)
    # 이미지 fixme

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('menu_detail', kwargs={"slug": self.slug})

    class Meta:
        ordering = ["id", "name_eng"]



class HandDrip(models.Model):
    region = models.CharField(max_length=120, null=False, blank=False)
    region_eng = models.CharField(max_length=120, null=False, blank=False)
    name = models.CharField(max_length=120, null=False, blank=False)
    name_eng = models.CharField(max_length=120,null=False, blank=False)
    slug = models.SlugField(unique=True, null=True, blank=True)
    description = models.TextField()
    price = models.PositiveIntegerField(null=False, blank=False)
    on_sale = models.BooleanField(default=True)
    roasting_date = models.DateField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('menu_detail', kwargs={'slug': self.slug})

    class Meta:
        ordering = ["-roasting_date", "-id"]


class Desert(models.Model):
    name = models.CharField(max_length=120, null=False, blank=False)
    name_eng = models.CharField(max_length=120, null=False, blank=False)
    slug = models.SlugField(unique=True, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    price = models.PositiveIntegerField(null=False, blank=False)
    on_sale = models.BooleanField(default=True)
    image = models.ImageField(upload_to='%Y/%m/%d/', null=True, blank=True)
    category = models.ForeignKey(Category)

    def __str__(self):
        return self.name

class DutchOrder(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    # phone_regex
    # phone_number = models.CharField(validators['phone_regex'], null=False, blank=True)
    # fixme
