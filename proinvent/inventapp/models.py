from django.db import models

# Create your models here.
class Items(models.Model):
    product_code = models.CharField(max_length=10, unique=True)
    product_name = models.CharField(max_length=30)
    quantity = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.product_name
