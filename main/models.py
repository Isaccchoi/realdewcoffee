from django.db import models

# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='images/%Y/%m/%d', null=True, blank=True)

    def __str__(self):
        return self.name
