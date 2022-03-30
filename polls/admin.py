from unicodedata import category
from django.contrib import admin
from polls.models import *
from polls.views import coupon, stocklist

# Register your models here.
admin.site.register(User)
admin.site.register(Product)
admin.site.register(Productslist)
admin.site.register(Stocklist)
admin.site.register(Address)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Category)
admin.site.register(Payments)
admin.site.register(SignupCoupon)
admin.site.register(Coupen)
