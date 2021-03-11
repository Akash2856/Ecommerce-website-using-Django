from django.db import models

class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=100, default = "")
    tagline = models.CharField(max_length=100, default = "")
    mrp = models.IntegerField(default=0)
    sp = models.IntegerField(default=0)
    Discount = models.IntegerField(default=0)
    image = models.ImageField(upload_to="accounts/img", default="")

    def __str__(self):
        return self.product_name


class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json= models.CharField(max_length=2000, default = "")
    name = models.CharField(max_length=90, default = "")
    email = models.CharField(max_length=100, default = "")
    address = models.CharField(max_length=200, default = "")
    city = models.CharField(max_length=100, default = "")
    state = models.CharField(max_length=100, default = "")
    zip_code = models.CharField(max_length=100, default=0)
    phone = models.CharField(max_length=100, default = 0)