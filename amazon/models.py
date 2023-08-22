from django.db import models

# Create your models here.
class products(models.Model):
    product=models.CharField(max_length=250)
    price=models.IntegerField()

