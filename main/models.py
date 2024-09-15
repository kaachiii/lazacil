# Create your models here.
import uuid
from django.db import models

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    location = models.TextField()
    quantity = models.IntegerField()

    @property
    def is_price_valid(self):
        return self.price > 0