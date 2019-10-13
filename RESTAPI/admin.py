from django.contrib import admin
from RESTAPI.models import ClothPicture, Order, OrderDetail, User, ClothingUnit
# Register your models here.

admin.site.register(ClothPicture)
admin.site.register(Order)
admin.site.register(OrderDetail)
admin.site.register(User)
admin.site.register(ClothingUnit)
