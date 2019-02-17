from django.db import models
from django.contrib.auth.models import User

class Restaurant(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete = models.CASCADE, default=1)
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    logo = models.ImageField(upload_to='restaurant_logos', null=True, blank=True)

    def __str__(self):
    	return self.name



class Item(models.Model):
    """
    Description: Item
    """
    name = models.CharField(max_length=40)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=7)
    restaurant = models.ForeignKey(Restaurant, on_delete = models.CASCADE, default=1, related_name='items')

    def __str__(self):
    	return self.name