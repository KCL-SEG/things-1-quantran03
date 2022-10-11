from django.db import models
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator

class Thing(models.Model):
    name = models.CharField(max_length=30, blank=False, unique=True)
    description = models.CharField(max_length=30, blank=True, unique=False)
    quantity = models.IntegerField(unique=False, validators=[
        MaxValueValidator(limit_value=100, message='Value must not be higher than 100.'),
        MinValueValidator(limit_value=0, message='Value must not be lower than 0.'),
        ])