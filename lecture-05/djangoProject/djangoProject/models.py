from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50)
    title = models.CharField(max_length=50,choices=[('Mr', 'Mr'), ('Ms', 'Ms'),('Mrs','Mrs')],default='Mr')
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    address = models.CharField(max_length=255,null=True)

class Product(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    name = models.CharField(max_length=50)
    price = models.FloatField()
    description = models.TextField(max_length=255)
    stock = models.IntegerField()
