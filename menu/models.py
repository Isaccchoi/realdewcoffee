from django.db import models

# Create your models here.

class Coffee(models.Model):
    name = models.CharField(max_length=120, null=False, blank=False)
    name_eng = models.CharField(max_length=120, null=True, blank=True)
    price = models.PositiveIntegerField(null=False, blank=False)
    description = models.TextField()
    on_sale = models.BooleanField(default=True)
    # 이미지

    def __unicode__(self):
        self.name



class Tea(models.Model):
    name = models.CharField(max_length=120, null=False, blank=False)
    name_eng = models.CharField(max_length=120, null=True, blank=True)
    price = models.PositiveIntegerField(null=False, blank=False)
    description = models.TextField()
    on_sale = models.BooleanField(default=True)

    def __unicode__(self):
        self.name



class Desert(models.Model):
    name = models.CharField(max_length=120, null=False, blank=False)
    name_eng = models.CharField(max_length=120, null=True, blank=True)
    price = models.PositiveIntegerField(null=False, blank=False)
    description = models.TextField()
    on_sale = models.BooleanField(default=True)

    def __unicode__(self):
        self.name



class HandDrip(models.Model):
    region = models.CharField(max_length=120, null=False, blank=False)
    region_eng = models.CharField(max_length=120, null=True, blank=True)
    name = models.CharField(max_length=120, null=False, blank=False)
    name_eng = models.CharField(max_length=120,null=True, blank=True)
    description = models.TextField()
    price = models.PositiveIntegerField(null=False, blank=False)
    on_sale = models.BooleanField(default=True)
    roasting_date = models.DateTimeField()

    def __unicode__(self):
        self.name
