from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

choices = (
    ("Red", "Red"),
    ("Black", "Black"),
    ("Blue", "Blue"),
)

class User(AbstractUser):
    """
    Customize django User functionality
    """
    contact_number = models.CharField(('Contact Number'), max_length=32)
    email = models.EmailField(null=True, blank=True)
    join_date = models.DateField(default=None, auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class ClothingUnit(models.Model):
    name = models.CharField(max_length=200, default="kurta")
    article_number = models.CharField(max_length=200)
    price = models.FloatField(default=0)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.article_number


class ClothPicture(models.Model):
    picture = models.FileField()
    color = models.CharField(choices=choices, max_length=100)
    clothing = models.ForeignKey(ClothingUnit, on_delete=models.CASCADE)

    def __str__(self):
        return self.color


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    total_amount = models.FloatField(default=0)
    order_date = models.DateField(auto_now_add=True)


class OrderDetail(models.Model):
    item = models.ForeignKey(ClothPicture, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)