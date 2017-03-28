from django.db import models
from django.core.validators import RegexValidator


# Create your models here.
from main.models import User


class Beverage(models.Model):
    name = models.CharField(max_length=50, unique=True)
    price = models.PositiveSmallIntegerField()
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_price(self):
        return self.price



beverage_trans ={
    "seogyo": "서교동 라떼",
    "dutch": "더치 커피",
}


class Order(models.Model):
    beverage = models.ForeignKey(Beverage)
    user = models.ForeignKey(User)
    quantity = models.PositiveSmallIntegerField(null=False, blank=False, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    reserve_at = models.DateTimeField(null=False, blank=True)
    total_charge = models.PositiveIntegerField(null=False, blank=False)
    pin = models.IntegerField(null=True, blank=False)


    def __str__(self):
        return self.user.phone_number

    def get_beverage_name(self):
        return beverage_trans[self.beverage.name]


    class Meta:
        ordering = ['-created_at', '-id']


#
#
# class SeogyodongOrder(models.Model):
#     user = models.ForeignKey(User)
#     quantity = models.PositiveSmallIntegerField(null=False, blank=False, default=1)
#     created_at = models.DateTimeField(auto_now_add=True)
#     reserve_at = models.DateTimeField(null=False, blank=True)
#     total_charge = models.PositiveIntegerField(null=False, blank=False)
#
#     def __str__(self):
#         return self.user.phone_number
#
#     class Meta:
#         ordering = ['-created_at', '-id']
