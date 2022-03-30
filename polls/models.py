from xml.etree.ElementTree import QName
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    phone = models.CharField(max_length=50)
    status=models.BooleanField(default=True,null=True)
    ref_id = models.CharField(max_length=50, null=True)
    

    def ___str___(self):
        return self.username


class Admin(models.Model):
    phone = models.CharField(max_length=50)
    status=models.BooleanField(default=True,null=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    

    def ___str___(self):
        return self.Username,str(self.id)
    



class Category(models.Model):
    category_name = models.CharField(max_length=50)
    category_off = models.IntegerField(default=0)


    def __str__(self):
        return str(self.category_name)


    


    
class Product(models.Model):
    name=models.CharField(max_length=100,null=True)
    brand=models.CharField(max_length=100,null=True)
    storage=models.CharField(max_length=100,null=True)
    RAM=models.CharField(max_length=100,null=True)
    display=models.CharField(max_length=100,null=True)
    processor=models.CharField(max_length=100,null=True)
    OS=models.CharField(max_length=100,null=True)
    battery=models.CharField(max_length=100,null=True)
    price=models.FloatField(null=True)
    image1=models.ImageField(upload_to='images',blank=True)
    image2=models.ImageField(upload_to='images',blank=True)
    image3=models.ImageField(upload_to='images',blank=True)
    image4=models.ImageField(upload_to='images',blank=True)
    stock =models.IntegerField(null=True)
    product_category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True) 
    product_off = models.IntegerField(default=0)

    
    def __str__(self):
        return self.name


    @property
    def offer(self):
        if self.product_off != 0 or self.product_category.category_off != 0:
            return self.product_category.category_off if self.product_off < self.product_category.category_off else self.product_off

    @property
    def last_price(self):
        if self.product_off != 0 and self.product_category.category_off != 0:
            if self.product_off < self.product_category.category_off:
                price = self.price - (self.price * self.product_category.category_off / 100)
            else:
                price = self.price - (self.price * self.product_off / 100)
        elif self.product_off != 0:
            price = self.price - (self.price * self.product_off / 100)
        elif self.product_category.category_off != 0:
            price = self.price - (self.price * self.product_category.category_off / 100)
        else:
            price = self.price
        return price






class Productslist(models.Model):
    image=models.ImageField(upload_to='images',blank=True)
    name=models.CharField(max_length=100,null=True)
    price=models.FloatField(null=True)
    
    
    def __str__(self):
        return self.name


class Stocklist(models.Model):
    image=models.ImageField(upload_to='images',blank=True)
    name=models.CharField(max_length=100,null=True)
    stock=models.FloatField(null=True)
    
    
    def __str__(self):
        return self.name



class Address(models.Model):
	aname = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	fname=models.CharField(max_length=30, null=True)
	lname=models.CharField(max_length=30, null=True)
	address = models.TextField(max_length=200, null=False)
	city = models.CharField(max_length=30, null=False)
	state = models.CharField(max_length=20, null=False)
	phone = models.CharField(max_length=11,null=True)
	pincode = models.IntegerField(null=False)
	

	def __str__(self):
		return self.address




class Order(models.Model):
    STATUS = ('Placed','Placed'),('shipped','shipped'),('Delivered','Delivered'),('Cancelled','Cancelled'),('UserCancelled','UserCancelled') ,('Out Of Delevery','Out Of Delevery'),('Return','Return') 
    # STATUS = (('New','New'),('Pending','Pending'),('shipped','shipped'),('Delivered','Delivered'),('Cancelled','Cancelled'),('UserCancelled','UserCancelled') ,('Placed','Placed'),('Out Of Delevery','Out Of Delevery'),('Return','Return') )
    user = models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    address = models.ForeignKey(Address,on_delete=models.SET_NULL, null=True)
    date_order = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length = 200,choices = STATUS, default = 'New', null=True)
    order_status = models.BooleanField(null=True,default=False)
    complete = models.BooleanField(null=True,default=False)   #added as an experiment and it is working now
    # payment = models.BooleanField(null=True, default = False)   
    buyNow = models.BooleanField(null=True,default=False)
    coupen = models.IntegerField(null=True) 

    def __str__(self):
        return str(self.id)
    
    @property
    def get_cart_total(self):
        order_items = self.orderitem_set.all()
        total = sum([item.get_total for item in order_items])
        if self.coupen is not None:
            total -= (total * float(self.coupen))/100
        return total
    
    @property
    def get_cart_items(self):
        order_items = self.orderitem_set.all()
        total = sum([item.quantity for item in order_items])
        return total

   


class OrderItem(models.Model):
    product = models.ForeignKey(Product,on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order,on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(default=1)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return str(self.order)

    @property
    def get_total(self):
        total = self.product.last_price * self.quantity
        return total



class Payments(models.Model):
    
    total_amount = models.FloatField(max_length=30,default=0,null=True)
    payment_method = models.CharField(max_length=30,null=True)
    payment_status = models.BooleanField( default=False )
    order =  models.OneToOneField(Order, on_delete=models.CASCADE , null=True)  
    transaction_id = models.CharField(max_length= 100,null= True ,blank=True)
    status = models.CharField(max_length=100,null = True, blank= True)


class SignupCoupon(models.Model):
    TYPE = (('Normal','Normal'),('ReferredTo','ReferredTo'),('ReferredBy','ReferredBy'))
    name = models.CharField(max_length=200, choices = TYPE, null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    price = models.CharField(max_length=200, null=True)
    available = models.BooleanField(null=True, default = True)
    proceed = models.BooleanField(null=True, default = False)

    def _str_(self):
        return self.name



class Coupen(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.CharField(max_length=200, null=True)
    available = models.BooleanField(null=True, default = True)
    proceed = models.BooleanField(null=True, default = False)
    remaining = models.IntegerField()



class WishList(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product,on_delete=models.SET_NULL, null=True)


