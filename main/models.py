# Create your models here.
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    quantity = models.IntegerField()
    rating = models.FloatField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    
    @property
    def is_price_valid(self):
        return self.price > 0