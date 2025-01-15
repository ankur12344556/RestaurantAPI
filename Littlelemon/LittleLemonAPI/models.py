from django.db import models

# Create your models here.
class Category(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=255)



class MenuItem(models.Model):
    title = models.CharField( max_length=255)
    price = models.DecimalField( max_digits=5, decimal_places=2)
    inventory = models.SmallIntegerField()
    Category = models.ForeignKey(Category, on_delete=models.PROTECT, default = 1)
    