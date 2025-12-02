from django.db import models

# Create your models here.
class Meal(models.Model):
    week_day = models.CharField(max_length=120)
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=2)
    taste = models.CharField(max_length=2)
    servings = models.CharField(max_length=2)
    notes = models.TextField()