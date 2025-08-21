from django.db import models

# Create your models here.

class Cosmetic(models.Model):
     name=models.CharField(max_length=100)
     price=models.DecimalField(max_digits=10, decimal_places=2)
     description=models.TextField(max_length=200, null=True, blank=True)
     image=models.ImageField(upload_to='photos/%y/%m/%d')
     active=models.BooleanField(default=True)

     def __str__(self):
        return self.name
     






class LoginCosmetic(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=100, null=True, blank=True)
    address=models.CharField(null=True, blank=True)
    product=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name