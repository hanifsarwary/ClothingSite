from django.contrib import admin
from RESTAPI.models import ClothPicture, Order, OrderDetail, User, ClothingUnit, Customer
# Register your models here.

admin.site.register(ClothPicture)
admin.site.register(Order)
admin.site.register(OrderDetail)
admin.site.register(Customer)
admin.site.register(ClothingUnit)
