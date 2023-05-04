from django.db import models

# Create your models here.


class SubType(models.Model):
    PRODUCT_TYPE = [
        ("com", "Comida"),
        ("beb", "Bebida"),
        ("otr", "Otro"),
    ]
    name = models.CharField(max_length=20)
    product_type = models.CharField(max_length=3, choices=PRODUCT_TYPE)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=200)
    subproduct_type = models.ForeignKey(SubType, on_delete=models.CASCADE)
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='product-images/', null=True)

    def __str__(self):
        return self.name


class TableSizes(models.Model):
    size_name = models.CharField(max_length=20)


class Location(models.Model):
    location_name = models.CharField(max_length=20)
    description = models.TextField(max_length=200)


class Table(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    size = models.ForeignKey(TableSizes, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Sale(models.Model):
    table = models.OneToOneField(Table, on_delete=models.DO_NOTHING)
    sale_name = models.CharField(max_length=40)
    date = models.DateTimeField(auto_now_add=True)
    # total_sale = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.sale_name


class SaleProduct(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    amount = models.IntegerField()

    def __str__(self):
        return self.product.name
