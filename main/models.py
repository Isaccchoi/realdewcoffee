from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='images/%Y/%m/%d', null=True, blank=True)

    def __str__(self):
        return self.name


class DutchOrder(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    phone_regex = RegexValidator(
                        regex="r^01([0|1|6|7|8|9]?)-?([0-9]{3,4})-?([0-9]{4})$",
                        message="010-1234-5678 형식으로 10~12자리를 입력하세요.")
    phone_number = models.CharField(max_length=13, validators = ['phone_regex'],
                        null=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    reserve_at = models.DateTimeField(null=False, blank=False)
    quantity = models.PositiveSmallIntegerField(null=False, blank=False)
    total_charge = models.PositiveIntegerField(null=False, blank=False)


    # fixme

    def __str__(self):
        return self.name
