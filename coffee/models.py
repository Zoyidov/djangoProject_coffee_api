from django.db import models

# Create your models here.
from django.db import models


class Coffee(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='coffee/images/')
    description = models.TextField()

    def __str__(self):
        return self.name
