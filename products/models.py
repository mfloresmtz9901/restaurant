from django.db import models

# Create your models here.


class Product(models.Model):
    PRODUCT_TYPE = [
        ("com", "Comida"),
        ("coc", "Cocteleria"),
    ]
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=200)
    product_type = models.CharField(max_length=3, choices=PRODUCT_TYPE)
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='product-images/', null=True)
