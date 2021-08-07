from django.db import models

# Create your models here.
class Item(models.Model):
   name  = models.CharField(max_length=100)
   quantity = models.PositiveIntegerField()
   brand = models.CharField(max_length=80, default="Unknown")

   def __repr__(self):
      return f"Item: {self.name} q: {self.quantity}"
