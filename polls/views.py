from multiprocessing import context
from venv import create
from django.http import JsonResponse
from http.client import responses
from django.views.decorators.cache import never_cache
from twilio.rest import Client
import random
from django.shortcuts import redirect, render
from .models import *
import datetime
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from decouple import config
from django.db.models import Sum
from .utils import *
from django.http import HttpResponse
import csv
import xlwt
# Create your views here.

@never_cache
def loginView(request):
    # if request.session.has_key('bmw'):
    #     return redirect('cosmic')
    if request.method=='POST':
        val6=request.POST.get("username")
        val7=request.POST.get("password")
         
             

        # print('/////////////////////////',val6,val7)
        user=None
        user = authenticate(request,username=val6,password=val7)
        print(user)
        try:
            user=User.objects.get(username=val6,password=val7)
            print('???????????????????????????',user)
        except:
            pass
        # print('/////////////////?????????????????????',authenticate(username=val6,password=val7))
        if user is not None:
           print("prathiksha")
           request.session['bmw']=val6
           print(request.session['bmw'],'this is bmw')
           login(request,user)
           return redirect('cosmic')
        else:
            print("othilla")
            print(user)
            error="username or password is not valid"
            return render(request,'login.html', {'error' : error} )
    return render(request,'login.html') 


@never_cache
def userlogout(request):
    # try:
    #     print('this is try')
    #     print(request.session['bmw'],'this is session')
    #     del request.session['bmw']
    # except:
    #     print('this is except')
    #     pass
    # if request.session.has_key('bmw'):
    #     del request.session['bmw']
    #     print('yes')
    #     return redirect('login')
    # else:
    #     print('no')
    #     print(request.session)
    #     return redirect('login')

    logout(request)            # should use this when authenticate middleware is used. do not use normal session 
                               # when all other things are working on authenticate. only use one 
    return redirect('login')


# def userlogin(request):
#     if request.user.is_authenticated:
#         return redirect('cosmic')
#     if request.method == "POST":
#         uname = request.POST.get('username')
#         password= request.POST.get('password')
#         try:
#             user = User.object.get(username=uname)
#         except:
#             messages.error(request,'User does not exists')
        
#         try:
#             user= authenticate(request,username=uname,password=password)
#             if user.adminstatus == False:
#                 if user is not None:
#                     login(request,user)
#                     return redirect ("UserHome")   
#             else:
#                 messages.error(request,"You have been banned by the admin. Please call our customer care for more details!")
#         except:
#             messages.error(request,'Invalid Password')
            
#         # print(user.username,user.password)
        
#     return render(request, "login.html")






    


# @never_cache
# def signup(request):
#     if request.session.has_key('bmw'):
#         return redirect('home')
#     if request.method =='POST':

#         val1=request.POST.get("username")
#         val2=request.POST.get("email")
#         val3=request.POST.get("phone")
#         val4=request.POST.get("password")
#         val5=request.POST.get("confirm")
       

#         if val4==val5:
#             user = User.objects.create(username=val1,email=val2,phone=val3,password=val4)
#             user.save()
        
#             return render(request,'cosmic.html')
#     else:
#         return render(request,'signup.html')    


# this code is to be used in terms of emergency conditions 


# @never_cache
# def signup(request):
#     if request.session.has_key('bmw'):
#         return redirect('cosmic')
#     elif request.method == 'POST':
#         val3 = request.POST.get("username")
#         val4 = request.POST.get("password")
#         val5 = request.POST.get("confirm")
#         val6 = request.POST.get("email")
#         val7=request.POST.get("phone")
#         uname = None
#         umail = None
        
#         print(val3,val4)
#         try:
#             uname = User.objects.get(username = val3)
#         except:
#             pass
#         try:
#             umail = User.objects.get(email = val6)
#         except:
#             pass
#         if uname is not None:
#             err = 'user name already taken'
#             return render(request, 'signup.html', {'uname':err})
#         elif umail is not None:
#             err = 'email name already taken'
#             return render(request, 'signup.html', {'umail':err})
#         elif 4 >= len(val4):
#             err = 'Password shold have minimum 5 chareters'
#             return render(request, 'signup.html', {'pass':err})
#         elif val4 != val5:
#             print('hrr1')
#             err = 'Password not match'
#             return render(request, 'signup.html', {'upass':err})
#         else:
#             print('hrr2')
#             user = User.objects.create(username = val3, password = val4, email = val6,phone = val7)
#             user.save()
#             request.session['bmw'] = val3
#             login(request,user)
#             return redirect('cosmic')
#     else:
#         return render(request,'signup.html') 



@never_cache
def signup(request, **kwargs):
    ref_code = kwargs.get('ref_code')
    if request.session.has_key('bmw'):
        return redirect('cosmic')
    elif request.method == 'POST':
        val3 = request.POST.get("username")
        val4 = request.POST.get("password")
        val5 = request.POST.get("confirm")
        val6 = request.POST.get("email")
        val7=request.POST.get("phone")
        uname = None
        umail = None
        
        print(val3,val4)
        try:
            uname = User.objects.get(username = val3)
        except:
            pass
        try:
            umail = User.objects.get(email = val6)
        except:
            pass
        if uname is not None:
            err = 'user name already taken'
            return render(request, 'signup.html', {'uname':err})
        elif umail is not None:
            err = 'email name already taken'
            return render(request, 'signup.html', {'umail':err})
        elif 4 >= len(val4):
            err = 'Password shold have minimum 5 chareters'
            return render(request, 'signup.html', {'pass':err})
        elif val4 != val5:
            print('hrr1')
            err = 'Password not match'
            return render(request, 'signup.html', {'upass':err})
        else:
            if ref_code == None:
                print('hrr2')
                user = User.objects.create(username = val3, password = val4, email = val6,phone = val7,ref_id = getRefcode(request))
                user.save()
                request.session['bmw'] = val3
                login(request,user)
                SignupCoupon.objects.create(name='Normal', user=user, price='10%')
                return redirect('cosmic')

            else:
                try:
                    user = None
                    user = User.objects.get(ref_id=ref_code)
                except:
                    pass
                if user is not None:
                    SignupCoupon.objects.create(name='ReferredBy', user=user, price='8%')
                    user = User.objects.create(username = val3, password = val4, email = val6,phone = val7)
                    user.save()
                    username = val3
                    User.objects.filter(username=username).update(ref_id = getRefcode(request))
                    user = User.objects.get(username=username)
                    SignupCoupon.objects.create(name='ReferredTo', user=user, price='18%')
                    request.session['bmw'] = val3
                    login(request,user)
                    return redirect('cosmic')

    else:
        return render(request,'signup.html') 





# @never_cache
# def sign_up(request, **kwargs):
#     ref_code = kwargs.get('ref_code')
#     form = UserForm()
#     if request.method == 'POST':
#         number = request.POST.get('phone')
#         otp = request.POST.get('otp')
#         check = otpCheck(request, number, otp)
#         if check == False:
#             try:
#                 const.stored = UserForm(request.POST)
#             except:
#                 pass
#             return render(request, 'users/sign_up.html',{'otp':True,'number':number,'message':'invalid OTP'})
#         else:
#             try:
#                 if const.stored != None:
#                     form = const.stored
#             except:
#                 form = UserForm(request.POST)
#             if ref_code == None:
#                     if form.is_valid():
#                         form.save()
#                         username = form['username'].value()
#                         User.objects.filter(username=username).update(ref_id = getRefcode(request))
#                         user = User.objects.get(username=username)
#                         SignupCoupon.objects.create(name='Normal', user=user, price='10%')
#                         login(request,user)
#                         return redirect('home')
#             else:
#                 try:
#                     user = None
#                     user = User.objects.get(ref_id=ref_code)
#                 except:
#                     pass
#                 if user is not None:
#                     if form.is_valid():
#                         form.save()
#                         SignupCoupon.objects.create(name='ReferredBy', user=user, price='8%')
#                         username = form['username'].value()
#                         User.objects.filter(username=username).update(ref_id = getRefcode(request))
#                         user = User.objects.get(username=username)
#                         SignupCoupon.objects.create(name='ReferredTo', user=user, price='18%')
#                         login(request,user)
#                         return redirect('home')
#     return render(request, 'users/sign_up.html', {'form':form})




def checkout(request):
    if request.user.is_authenticated:
        user = request.user
        coupens = user.signupcoupon_set.filter(available = False, proceed=False)
        for coupen in coupens:
            SignupCoupon.objects.filter(id=coupen.id).update(available = True)
        order = Order.objects.get(user=user,order_status=False,buyNow=False)
        items = order.orderitem_set.all()
        address = Address.objects.filter(user=user)
        coupens = user.signupcoupon_set.filter(available = True)
        return render(request, 'users/checkout.html', {'order':order,'items':items,'address':address,'coupens':coupens})
    else:
        return redirect('email_login')





# @never_cache
# def adminlogin(request):   
#     if request.method == "POST":
#         print('test1')
#         val1 = request.POST.get("username")
#         val2 = request.POST.get("password")
         
#         if val1 == 'hrishi' and val2 == 'hrishi':
#             return render(request,'admin2.html')
#         else:
#             error = "invalid entry"
#             return render(request,'adminlogin.html',{ 'error' : error })
 
#     return render(request,'adminlogin.html')



@never_cache
def adminlogin(request):
    if request.user.is_authenticated:
        return redirect('admin2')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username= username , password = password)
        if user is not None :
            user_is = User.objects.get(username = username)
            if user_is.is_superuser == True:
                login(request, user)
                return redirect('admin2')
            else:
                messages.error(request,"You have no access to admin page")
        else:
            messages.error(request,"Incorrect UserName or Password")
    return render(request, 'adminlogin.html')


@never_cache
def adminlogout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("adminlogin")



# @never_cache
# def adminlogout(request):
#     return render(request,'adminlogin.html')




# def razorpay(request):
#     return()



             

     




@never_cache
def admin_signup(request):
    if request.session.has_key('bmw'):
        return redirect('home')
    if request.method == 'POST':
        val3 = request.POST.get("username")
        val4 = request.POST.get("password")
        val5 = request.POST.get("confirm")
        val6 = request.POST.get("email")
        val7=request.POST.get("phone")
        uname = None
        umail = None
        
        print(val3,val4)
        try:
            uname = Admin.objects.get(username = val3)
        except:
            pass
        try:
            umail = Admin.objects.get(email = val6)
        except:
            pass
        if uname is not None:
            err = 'user name already taken'
            return render(request, 'adminsignup.html', {'uname':err})
        elif umail is not None:
            err = 'email name already taken'
            return render(request, 'adminsignup.html', {'umail':err})
        elif 4 >= len(val4):
            err = 'Password shold have minimum 5 chareters'
            return render(request, 'adminsignup.html', {'pass':err})
        elif val4 != val5:
            print('hrr1')
            err = 'Password not match'
            return render(request, 'adminsignup.html', {'upass':err})
        else:
            print('hrr2')
            adminuser = Admin.objects.create(adminusername = val3, password = val4, email = val6,phone = val7)
            adminuser.save()
            request.session['bmw'] = val3
            return redirect('cosmic')
    else:
        return render(request,'adminsignup.html') 
        






# def cosmic(request):
#     available = False
#     if request.user.is_authenticated:
#         try:
#             cart = json.loads(request.COOKIES['cart'])
#         except:
#             cart ={}
#         if bool(cart):
#             user = request.user
#             order , created = Order.objects.get_or_create(user=user,order_status=False,buyNow=False)
#             for i in cart:
#                 product = Product.objects.get(id=i)
#                 try:
#                     item = None
#                     item = OrderItem.objects.get(product=product, order=order)
#                 except:
#                     item = OrderItem.objects.create(product=product,order=order,quantity=0)
#                     pass
#                 if item is not None:
#                     quantity = int(item.quantity) + cart[i]['quantity']
#                     OrderItem.objects.filter(product=product, order=order).update(quantity=quantity)
#             available = True
#     item = Product.objects.all()
#     user = request.user
#     print(user,'............')
#     return render(request,'cosmic.html',{'products' : item,'available' : available})



def cosmic(request):
    available = False
    wishList = []
    if request.user.is_authenticated:
        try:
            cart = json.loads(request.COOKIES['cart'])
        except:
            cart ={}
        if bool(cart):
            user = request.user
            order , created = Order.objects.get_or_create(user=user,order_status=False,buyNow=False)
            for i in cart:
                product = Product.objects.get(id=i)
                try:
                    item = None
                    item = OrderItem.objects.get(product=product, order=order)
                except:
                    item = OrderItem.objects.create(product=product,order=order,quantity=0)
                    pass
                if item is not None:
                    quantity = int(item.quantity) + cart[i]['quantity']
                    OrderItem.objects.filter(product=product, order=order).update(quantity=quantity)
            available = True
        user = request.user
        print(user,'............')
        wishList = [item.product.id for item in WishList.objects.filter(user=user)]
    item = Product.objects.all()
    category = Category.objects.all()
    return render(request,'cosmic.html',{'products' : item,'available' : available,'wishList':wishList ,'category' : category })





def wishItems(request):
    wishList = []
    if request.user.is_authenticated:
        user = request.user
        wishList = [item.product for item in WishList.objects.filter(user=user)]
        try:
            order = Order.objects.get(user=user,order_status=False,buyNow=False)  #here is an error
        except:
            order = {}
    count = len(wishList)
    return render(request, 'wishlist.html', {'products':wishList,'order':order,'count':count})




def wishList(request):
    print('..........michu und')
    productId = request.GET.get('product_id')
    product = Product.objects.get(id=productId)
    user = request.user
    products = WishList.objects.filter(user=user,product=product)
    wishList = [item.product for item in WishList.objects.filter(user=user)]
    if len(products) == 0 :
        WishList.objects.create(user=user,product=product)
        action = 'add'
        count = int(len(wishList)) + 1
    else:
        products.delete()
        action = 'remove'
        count = int(len(wishList)) - 1
    return JsonResponse({'id':productId,'action':action,'count':count})










def profile(request):
    user = request.user
    print(user,'this is user')
    person = User.objects.get(username = user)
    form= MyAddressForm()
    addr = Address.objects.filter(aname=user)
    return render(request,'profile.html',{ 'person' : person,'addr':addr,'form':form, })
    

def editprofile(request):
    user = request.user
    form = MyUserFormUser(instance=user)
    context = {'form' : form }
    if request.method == 'POST':
        form = MyUserFormUser(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return redirect('editprofile')
    return render(request,'editprofile.html',context)


def category(request,id='0'):
    print('this is id',id)
    if id != '0':
        print(type(id))
        print('this is if',id)
        category = Category.objects.get(id=id)
        items=Product.objects.filter(product_category_id=category)
    else:
        print('this is else',id)
        items = Product.objects.all()
    return render(request,'cosmic.html',{'products' : items })


def home(request):
    return render(request,'home.html')



def homein(request):
    return render(request,'login.html')
   

def admin2(request):
    print('\n\n\n\nhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh\n\n\n\n\n')
    products = Product.objects.all()

    placed = Order.objects.filter(status= 'Placed').count()
    shipped = Order.objects.filter(status= 'shipped').count()
    completed = Order.objects.filter(status= 'Completed').count()
    cancelled = Order.objects.filter(status= 'Cancelled').count()
    out_of_delivery = Order.objects.filter(status= 'Out Of Delevery').count()
    returned = Order.objects.filter(status= 'Return').count()
    order_status = [placed,shipped,out_of_delivery,completed,cancelled,returned]
    print(order_status,'................order status')

    cod = Payments.objects.filter(payment_method = 'COD').count()
    paypal = Payments.objects.filter(payment_method = 'Paypal').count()
    razorpay = Payments.objects.filter(payment_method = 'razorpay').count()
    payment_type = [cod,paypal,razorpay]

    print('......//.........',payment_type)
    
    orderitems = OrderItem.objects.filter(order= completed)
    print(orderitems,'....................payment mehod is here')
    

    customers = User.objects.all().count()
    orders = Order.objects.all().count()
    product_count = Product.objects.all().count()
    total_revenue = Payments.objects.all().aggregate(Sum('total_amount'))
   
   
    
    
    context = {'products':products,'order_status': order_status, 'payment_type': payment_type, 
     'customers':customers,'orders': orders, 'product_count':product_count,'total_revenue':total_revenue}
    return render(request,'admin2.html',context)
    


def userslist(request):
    person = User.objects.all().order_by('id')
    return render(request,'adminuserslist.html',{'userslist' : person})


def productslist(request):
    item = Product.objects.all().order_by('id')
    return render(request,'productslist.html',{'product' : item })


def couponlist(request):
    item = Coupen.objects.all().order_by('id')
    return render(request,'couponlist.html',{'coupon' : item })



def coupon_add(request):
    if request.method == "POST":
        name = request.POST['name']
        offer = request.POST['offer']
        stock = request.POST['stock']
        Coupen.objects.create(name = name,price = offer, remaining = 0)
    return render(request,'coupon_add.html')
    # return redirect('couponlist')

def coupon_edit(request):
    if request.method == "POST":
        id = request.POST.get('typeId')
        val = request.POST.get('val')
        Coupen.objects.filter(id = id).update(price=val)
    return redirect('couponlist')


def coupon_delete(request,id):
    Coupen.objects.filter(id=id).delete()
    return redirect('coupnlist')





def stocklist(request):
    stock = Stocklist.objects.all()
    return render(request,'stocklist.html', { 'stocklist' : stock } )





# def addproduct(request,id=0):
#     if id ==0:
#         form=MyProductForm()
#     else:
#         product = Product.objects.get(id=id)
#         form=MyProductForm(instance= product)
#     context={'form':form}
#     if request.method == 'POST':
#         form = MyProductForm(request.POST,request.FILES)    # here it will only create only a new product because there is no instance of the current product is given
#         if form.is_valid():
#             form.save()
#             return redirect('addproduct')
#     return render(request,'addproduct.html', context)



def addproduct(request,id=0):
    if id ==0:
        form=MyProductForm()
    else:
        product = Product.objects.get(id=id)
        form=MyProductForm(instance= product)
    context={'form':form}
    if request.method == 'POST':
        form = MyProductForm(request.POST,request.FILES)    # here it will only create only a new product because there is no instance of the current product is given
        if form.is_valid():
            form.save()
            messages.success(request,"data inserted successfully")
        else:
            messages.warning(request,"data was not inserted")
            return redirect('addproduct')
    return render(request,'addproduct.html', context)






def editproduct(request,id=0):
    if id ==0:
        form=MyProductForm()
    else:
        product = Product.objects.get(id=id)
        form=MyProductForm(instance= product)
    context={'form':form}
    if request.method == 'POST':
        form = MyProductForm(request.POST,request.FILES,instance=product)  # here instance is given in order to edit the corresponding product 
        if form.is_valid():
            form.save()
            return redirect('addproduct')
    return render(request,'addproduct.html', context)



def delete_product(request,id):
    item = Product.objects.get(pk=id)
    item.delete()
    return redirect('productslist')










def remove_order(request,id):
    item = OrderItem.objects.get(pk=id)
    item.delete()
    return redirect('user_checkout')


    

def product_details(request,id=0):
    product = Product.objects.get(id=id)
    return render(request,'product_details.html',{'product' : product})




# def user_checkout(request):
#     if request.method == 'GET':
#         try:
#             product_id = None
#             product_id = request.GET.get('productId')   # here we get product id from ajax
#             action = request.GET.get('action')
#             user = request.user
#             order = Order.objects.get(user=user,order_status=False)
#             product = Product.objects.get(id=product_id)
#             print(product)
#             order_item = OrderItem.objects.get(product=product, order=order)
#             print('in')
#             if str(action) == 'increment':
#                 quantity = int(order_item.quantity) + 1
#                 OrderItem.objects.filter(product=product, order=order).update(quantity=quantity)
#             elif str(action) == 'decrement' and order_item.quantity > 1:
#                 quantity = int(order_item.quantity) - 1
#                 OrderItem.objects.filter(product=product, order=order).update(quantity=quantity)
#             items = order.orderitem_set.all()
#             item = OrderItem.objects.get(product=product, order=order)
#             response = {'quantity': quantity,'id':product_id, 'cart_total':order.get_cart_total, 'item_total': item.get_total, 'total_items':order.get_cart_items,'stock':'items.product.stock' }
#             return JsonResponse(response)
#         except:
#             try:
#                 user = request.user
#                 order = Order.objects.get(user=user,order_status=False)
#                 items = order.orderitem_set.all()
#             except:
#                 order = []
#                 items = {}

#     if request.user.is_authenticated:
#         cust=request.user
#         print(cust)
#         order= Order.objects.get(user=cust,order_status=False)
#         items=order.orderitem_set.all()
#     else:
#         items=[]
#         order=[]
#     context={'itemss':items,'order':order}
#     return render(request,'user_checkout.html',context)



def user_checkout(request):
    if request.user.is_authenticated:
        user = request.user
        Order.objects.filter(user=user,order_status=False,buyNow=True).delete()
        print('...........sreejith',user)
        # order,created = Order.objects.get(user=user,status='New',order_status=False) # this is the old line that is existing
        # order= Order.objects.get(user=user,complete=False)

        try:
            Order.objects.filter(user=user,order_status=False,buyNow=False).update(coupen=None)
            order= Order.objects.get(user=user,order_status=False,buyNow=False)
            print('......this is order',order)
            items = order.orderitem_set.all()
        except:
            items=[]
            order=[]
    # else:
    #     items = []
    #     order=  []
    else:
        cookieData = cookieCart(request)              #this is coming from the cookies cart in utils.py
        order = cookieData['order']
        items = cookieData['items']
    # return render(request, 'users/cart.html',{'order':order,'items':items})  # this is the copied code from wafi
    context = {'itemss':items,'order':order}
    return render (request, "user_checkout.html",context)


        



def updatecart(request):
    
    if request.method == 'GET':
        try:
            product_id = None
            product_id = request.GET.get('productId')   # here we get product id from ajax
            action = request.GET.get('action')
            print('id',product_id,'\taction',action)
            user = request.user
            print("upadatecart",user)
            order,create  = Order.objects.get_or_create(user=user,order_status=False,buyNow=False)
            product = Product.objects.get(id=product_id)
            print(product)
            order_item,create = OrderItem.objects.get_or_create(product=product, order=order)
            print('in')
            if str(action) == 'increment':
                quantity = int(order_item.quantity) + 1
                OrderItem.objects.filter(product=product, order=order).update(quantity=quantity)
            elif str(action) == 'decrement' and order_item.quantity > 1:
                quantity = int(order_item.quantity) - 1
                OrderItem.objects.filter(product=product, order=order).update(quantity=quantity)
            # items = order.orderitem_set.all()
            item = OrderItem.objects.get(product=product, order=order)
            response = {'quantity': quantity,'id':product_id, 'cart_total':order.get_cart_total, 'item_total': item.get_total, 'total_items':order.get_cart_items,'stock':'items.product.stock' }
       
            return JsonResponse(response)
        except:
            try:
                user = request.user
                order = Order.objects.get(user=user,order_status=False,buyNow=False)
                items = order.orderitem_set.all()
            except:
                order = []
                items = {}
            







@never_cache
def otplogin(request):
    global number,phone
    if request.method == 'POST':
        phone = request.POST.get('number')
        number = '+91' + str(phone)
        user = None
        try:
            user = User.objects.get(phone=phone)
        except:
            messages.error(request,"No matching phone number found!")
            return render(request, 'otplogin.html') 
        if user is not None:
            account_sid = config('account_sid')
            auth_token = config('auth_token')
            client = Client(account_sid, auth_token)
            verification = client.verify \
                                .services(config('services')) \
                                .verifications \
                                .create(to=number, channel='sms')
            return redirect ('OtpVerify')
    return render(request,'otplogin.html')


@never_cache
def otpverify(request):
    user=User.objects.get(phone=phone)
    if request.method == 'POST':
        otp = request.POST.get('otp')
        account_sid = config('account_sid')
        auth_token = config('auth_token')
        client = Client(account_sid, auth_token)
        if(len(str(otp))==6):
            verification_check = client.verify \
                                .services(config('services')) \
                                .verification_checks \
                                .create(to= number, code= str(otp))
        else:
            messages.error(request,"Enter a valid OTP!")
            return render(request, 'otpverify.html')
        if verification_check.status == 'approved':
            login(request,user)
            return redirect('cosmic')
        else:
            messages.error(request,"Invalid OTP")
            return redirect ("OtpLogin")
    return render(request,'otpenter.html')



@never_cache
def otpsignup(request):
    print('ook')
    global regform
    User.objects.filter(is_active=False).delete()
    form= MyUserFormUser()
    if request.method == 'POST':
        form = MyUserFormUser(request.POST)
        uname=request.POST.get("username")
        print(uname)
        umail=request.POST.get("email")
        uphone=request.POST.get("phone")
        print(uphone)
        request.session['phone'] = uphone
        print(request.session['phone'])
        un="Not taken"
        um="Not taken"
        up="Not taken"
        
        try:
            un = User.object.get(username=uname)
            print(un)
            messages.error(request,"Username already taken")
        except:
            pass
    
        try:
            um = User.object.get(email=umail)
            messages.error(request,"Email already taken")
        except:
            pass
        
        try:
            up = User.object.get(phone=uphone)
            messages.error(request,"Phone number already taken")
        except:
            pass
        
        if un == "Not taken":
            print(form.errors)
            if(len(str(uphone))<=10):
                print(form.errors)
                if form.is_valid():
                    print('hello')
                    regform=form.save(commit=False)
                    regform.is_active=False
                    regform.save()
                    print('saved')
                    print(form.errors)
                    return redirect ("otpphone")
                else:
                    messages.error(request,"Enter the details properly!")
            else:
                messages.error(request,"Enter a 10 digit-number!")
        else:
            messages.error(request,"Username , email or phone already taken")
                
        
    context={'form':form}
    return render(request, "otpsignup.html",context)



@never_cache
def otpsignupverify(request):
    global regform
    number = request.session.get('phone')
    print(number)
    if request.method == 'POST':
        print("//////////////////////////this is verification")
        otp = request.POST.get('otp')
        print(otp,'this is the otp /////////////////////')
        account_sid = config('account_sid')
        auth_token = config('auth_token')
        client = Client(account_sid, auth_token)
        if(len(str(otp))==6):
            verification_check = client.verify \
                                .services(config('services')) \
                                .verification_checks \
                                .create(to= number, code= str(otp))
        else:
            messages.error(request,"Enter a valid OTP!")
            return render(request, 'otpenter.html')
        if verification_check.status == 'approved':
            regform.is_active=True
            regform.save()
            num=number[3:]
            print(num)
            user=User.objects.get(phone=num)
            login(request,user)
            return redirect('cosmic')
        else:
            messages.error(request,"Invalid OTP")
            return render (request,"otpenter.html")
    return render(request,'otpenter.html')


@never_cache
def otpphone(request):
    
    phone = request.session.get('phone')
    print("/////////////////////////////////////")
    print(phone)
    if request.method == 'POST':
        print("///////////////this is phone vefication")
        number = '+91' + str(phone)
        request.session['phone'] = number
        account_sid = config('account_sid')
        auth_token = config('auth_token')
        client = Client(account_sid, auth_token)
        verification = client.verify \
                            .services(config('services')) \
                            .verifications \
                            .create(to=number, channel='sms')
        return redirect ('otpsignupverify')
    return render(request,'otpphone.html',{'phone':phone})








# def otplogin(request):
    # global otp, number
    # if request.method == 'POST':
    #     otp = random.randrange(111111,999999)
    #     print(otp)
    #     number = str(request.POST.get('number'))
    #     try:
    #         user = User.objects.get(Phone=number)
    #     except:
    #         return render(request,'otplogin.html',{'message':'phone number does not exist'})
        # uname = user.Username
        # otp_body = str(uname) + ' ' + str(otp)

        # account_sid = 'ACa390880127c10ff156e62c1dd868996f' 
        # auth_token = '82d45c6e4bfea0685a3bc18cbc48be35' 
        # client = Client(account_sid, auth_token) 
 
        # message = client.messages.create(  
        #                       messaging_service_sid='MGed44aa6ecff383aedd1c82a92dc78cc5',
        #                       body= otp_body,     
        #                       to='+917012247169'
        #                   )  
 
      
        # return redirect('otpenter')
    # return render(request,'otplogin.html')







# @never_cache
# def otpsignup(request):
#     global otp,number
#     if request.session.has_key('bmw'):
#         return redirect('home')
#     elif request.method == 'POST':
#         otp = random.randrange(111111,999999)
#         print(otp)
#         number = str(request.POST.get('number'))
#         try:
#             user = User.objects.get(Phone=number)
#         except:
#             return render(request,'otplogin.html',{'message':'phone number does not exist'})
#         val3 = request.POST.get("username")
#         val4 = request.POST.get("password")
#         val5 = request.POST.get("confirm")
#         val6 = request.POST.get("email")
#         val7=request.POST.get("phone")
#         uname = None
#         umail = None
        
    #     print(val3,val4)
    #     try:
    #         uname = User.objects.get(username = val3)
    #     except:
    #         pass
    #     try:
    #         umail = User.objects.get(email = val6)
    #     except:
    #         pass
    #     if uname is not None:
    #         err = 'user name already taken'
    #         return render(request, 'signup.html', {'uname':err})
    #     elif umail is not None:
    #         err = 'email name already taken'
    #         return render(request, 'signup.html', {'umail':err})
    #     elif 4 >= len(val4):
    #         err = 'Password shold have minimum 5 chareters'
    #         return render(request, 'signup.html', {'pass':err})
    #     elif val4 != val5:
    #         print('hrr1')
    #         err = 'Password not match'
    #         return render(request, 'signup.html', {'upass':err})
    #     else:
    #         print('hrr2')
    #         user = User.objects.create(username = val3, password = val4, email = val6,phone = val7)
    #         user.save()
    #         request.session['bmw'] = val3
    #         return redirect('cosmic')
    # else:
    #     return render(request,'signup.html') 










# def otpenter(request):
#     if request.method == 'POST':
#         otpnumber=request.POST.get('otpnumber')
#         if str(otp) == str(otpnumber):
#             request.session['bmw']='phone number'
#             return redirect('cosmic')
            
#         else:
#             return render(request,'otpenter.html')
#     return render(request,'otpenter.html')


def otp_check(request):
    if request.method=='post':
        print('hello')
        otpnumber=str(request.POST.get('otpnumber'))
        if otpnumber is not None:
                if otpnumber==str(otp):
                    otpnumber = None
                    request.session['bmw'] = number
                    return redirect('cosmic')
                else:
                    return render(request,'otplogin.html', {'otperror' : 'otp is not matching','number':number})
    return render(request,'otplogin.html')


def block(request):
    if request.method == "POST":
        user_id = request.POST.get('id')
        btn_id = request.POST.get('btnId')
        user = User.objects.filter(id=user_id)
        status = [user.status for user in user]
        userStatus = status[0]
        if userStatus == True:
            user.update(status=False)
        else:
            user.update(status=True)
        response = {'status':userStatus,'btn':btn_id}
        return JsonResponse(response)
    return render(request,'home.html')

# def unblock(request):
#     if request.method == "POST":
#         user_id = request.POST.get('id')
#         User.objects.filter(id=user_id).update(status=True)
#         response = {}
#         return JsonResponse(response)
#     return render(request,'home.html')


# def addcart(request):
#     # if request.method == 'POST':
#     #      user_id = request.POST.get('id')
#     #      print(user_id)
         
#     if request.method == 'POST':
#         product_id = request.POST.get('product_id')
#         user = request.user
#         print(product_id, user)
#         order, create  = Order.objects.get_or_create(user=user,order_status=False)
#         product = Product.objects.get(id=product_id)
#         print('work') 
#         try:
#             item = None
#             item = OrderItem.objects.get(product=product,order=order)
#         except:
#             pass
#     if item is not None:
#         quantity = int(item.quantity) + 1
#         OrderItem.objects.filter(product=product, order=order).update(quantity=quantity)
#     else:
#         OrderItem.objects.create(product=product,order=order,quantity=1)    #here dont use Order instead of order because this is the order mentioned in 
#     return redirect('cosmic')                                     #the above code and - orderitem_set.all() is used to get all the elements from Order class and its a little bit confusing





def addcart(request):

    if request.method == 'GET':
        try:
            product_id = None
            product_id = request.GET.get('id')
            action = request.GET.get('action')
            user = request.user
            print("addcart ",user)
            
            order,created = Order.objects.get_or_create(user=user,order_status=False,status='Placed',buyNow=False)
            print(order)
            product, created = Product.objects.get(id=product_id)
            order_item = OrderItem.objects.get_or_create(product=product, order=order)

            if str(action) == 'increment':
                quantity = int(order_item.quantity) + 1
                OrderItem.objects.filter(product=product, order=order).update(quantity=quantity)
            elif str(action) == 'decrement' and order_item.quantity > 1:
                quantity = int(order_item.quantity) - 1
                OrderItem.objects.filter(product=product, order=order).update(quantity=quantity)

            items = order.orderitem_set.all()
            item = OrderItem.objects.get(product=product, order=order)
            response = {'quantity': quantity,'id':product_id, 'cart_total':order.get_cart_total, 'item_total': item.get_total, 'total_items':order.get_cart_items,'stock':'items.product.stock' }
            return JsonResponse(response)
        except:
            try:
                user = request.user
                order = Order.objects.get(user=user,order_status=False,buyNow=False)
                items = order.orderitem_set.all()
            except:
                order = []
                items = {}

    elif request.method == 'POST':
        if request.session.has_key('bmw'):
            print('yes')
            print(request.user)
            print(request.session.has_key('bmw'))
        product_id = request.POST.get('product_id')
        user = request.user
        print(product_id, user)
        try:
            order = Order.objects.get(user=user,order_status=False,buyNow=False)
        except:
            order = Order.objects.create(user=user,order_status=False,buyNow=False)
        print(order)
        product = Product.objects.get(id=product_id)
        try:
            
            items = OrderItem.objects.get(product=product,order=order)
        except:
            items = None
    if items is not None:
        quantity = int(items.quantity) + 1
        items = OrderItem.objects.filter(product=product, order=order).update(quantity=quantity)
    else:
        OrderItem.objects.create(product=product,order=order,quantity=1)
    order = Order.objects.get(user=user,order_status=False,buyNow=False)
    items = OrderItem.objects.filter(product=product,order=order)
    print(order,'order')
    hello = {'items':items,'order' : order }
    
    return render(request, 'user_checkout.html',hello)  





def buyNow(request,id):
    print('.................inside buy now')
    if request.user.is_authenticated:
        print('...............user is authenticated')
        user = request.user
        coupens = user.signupcoupon_set.filter(available = False, proceed=False)       #updation fishy
        for coupen in coupens:                                                         #updation fishy
            SignupCoupon.objects.filter(id=coupen.id).update(available = True)         #updation fishy
        print('//////////////check the user',user)                                     #updation fishy
        Order.objects.filter(user=user,order_status=False,buyNow=True).delete()
        order  = Order.objects.create(user=user,order_status=False,buyNow=True)
        product = Product.objects.get(id=id)
        OrderItem.objects.create(order=order,product=product)
        items = order.orderitem_set.all()
        address = Address.objects.filter(aname=user)
        signupcoupens = user.signupcoupon_set.filter(available = True) #updation fishy
        coupens = Coupen.objects.filter(remaining__gt=0)
        return render(request, 'user_payment.html', {'order':order,'product':product,'addr':address,'coupens' : coupens,'items':items,'signupCoupens':signupcoupens })
    else:
        return redirect('login')








def address(request):
    # if id ==0:
    #     form=MyAddressForm()
    # else:
    #     address = Address.objects.get(id=id)
    #     form=MyAddressForm(instance= address)
    # context={'form':form}
    if request.method == 'POST':
        form = MyAddressForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('user_payment')
    form=MyAddressForm()
    return render(request,'user_address.html',{'form' : form ,'flag' : False })



def editaddress(request,id=0):
    if id ==0:
        form=MyAddressForm()
    else:
        address_id = Address.objects.get(id=id)
        form=MyAddressForm(instance= address_id)
        flag = 1
    context={'form':form , 'flag' : flag , 'address_id' : address_id }
    if request.method == 'POST':
        form = MyAddressForm(request.POST,request.FILES,instance=address_id)  # here instance is given in order to edit the corresponding product 
        if form.is_valid():
            form.save()
            return redirect('user_payment')
    return render(request,'user_payment.html', context)







# this is the thing that you are looking for as user_payment old version

# def user_payment(request):
#     # form = MyAddressForm(instance=request.user)
#     if request.user.is_authenticated:
#         user = request.user
#         print('//////////////check the user',user)
#         # items = order.orderitem_set.all()
#         try:
#             order = Order.objects.get(user=user,order_status=False)
#             print('..............nice try')
#             items = order.orderitem_set.all()
#             print('..........',order.get_cart_total)
#             print('..........',order)
#         except:
#             order=  []
#             items = []
#             return redirect("user_checkout")
#     form= MyAddressForm()
#     if request.method == 'POST':
#         form = MyAddressForm(request.POST,request.FILES)
#         if form.is_valid():
#             a=form.save(commit=False)
#             a.aname=request.user
#             a.save()
#     addr = Address.objects.filter(aname=user)
#     context = {'order':order,'items':items,'addr':addr,'form':form}
#     return render(request,'user_payment.html',context)



def dlt_address(request):
    print('here delete address')
    add_id = request.GET.get('add_id')
    Address.objects.filter(id=add_id).delete()
    return JsonResponse({'id':add_id})


def add_address(request):
    if request.method == 'POST':
        form = MyAddressForm(request.POST,request.FILES)
        if form.is_valid():
            a=form.save(commit=False)
            a.aname=request.user
            a.save()
    return redirect("user_payment")


def user_payment(request):
    # form = MyAddressForm(instance=request.user)
    if request.user.is_authenticated:
        user = request.user
        coupens = user.signupcoupon_set.filter(available = False, proceed=False)
        for coupen in coupens:
            SignupCoupon.objects.filter(id=coupen.id).update(available = True)
        print('//////////////check the user',user)
        # items = order.orderitem_set.all()
        try:
            Order.objects.filter(user=user,order_status=False,buyNow=False).update(coupen=None)
            order = Order.objects.get(user=user,order_status=False)
            print('..............nice try')
            items = order.orderitem_set.all()
            print('..........',order.get_cart_total)
            print('..........',order)
        except:
            order=  []
            items = []
            return redirect("user_checkout")
    form= MyAddressForm()
    addr = Address.objects.filter(aname=user)
    signupcoupens = user.signupcoupon_set.filter(available = True)
    coupens = Coupen.objects.filter(remaining__gt=0)
    context = {'order':order,'items':items,'addr':addr,'form':form,'signupCoupens':signupcoupens,'coupens' : coupens}
    return render(request,'user_payment.html',context)


def checkout(request):
    if request.user.is_authenticated:
        user = request.user
        signupCoupens = user.signupcoupon_set.filter(available = False, proceed=False)
        for coupen in signupCoupens:
            SignupCoupon.objects.filter(id=coupen.id).update(available = True)
        order = Order.objects.get(user=user,order_status=False,buy_now=False)
        items = order.orderitem_set.all()
        address = Address.objects.filter(user=user)
        signupCoupens = user.signupcoupon_set.filter(available = True)
        coupens = Coupen.objects.filter(remaining__gt=0)
        return render(request, 'users/checkout.html', {'order':order,'items':items,'address':address,'coupens':coupens, 'signupCoupens':signupCoupens})
    else:
        return redirect('email_login')



def user_order(request):
    user =request.user
    try :
        print('........order working before')
        order = Order.objects.filter(user=user,order_status=True)
        print('........order working')
    except:
        order = []
    context = {'order' : order}
    return render(request,'user_order.html',context)


# the real working model of razorpay below 

def razorpay(request):
    user = request.user
    address_id = request.GET.get('address')
    address = Address.objects.get(id=address_id)
    order = Order.objects.get(user=user,order_status=False,buyNow=False)
     #added on purpuse on my own
    response={'total':order.get_cart_total,'name':address.fname,'email':address.aname.username,'phone':address.phone}
    return JsonResponse(response)

# the realworking model of razorpay above










# below is michu razorpay

# @ csrf_exempt
# def razorpay(request):
#     print('hello razorpay')
#     user=request.user
#     print(user)
#     if request.method == 'POST': 
#         try:
#             order= Order.objects.get(customer=user,complete=False,status="BuyNow")
#             print("/////////////////////////////////buynow")
#         except:
#             print("/////////////////////////////////cart")
#             order= Order.objects.get(customer=user,complete=False,status="New")
#         items = order.orderitem_set.all()
#         for item in items :
#             ordered = item.quantity
#             print(item.quantity)
#             prestocks = item.product.stocks
#             poststocks = prestocks - ordered
#             productid = item.product.id
#             Product.objects.filter(id = productid).update(stocks = poststocks)
#         total_amount = order.get_cart_total
#         transaction_id = request.POST.get('order_id')
#         Pay.objects.get_or_create(payuser=user,order = order,method = 'RazorPay',amount = total_amount,status = 'Completed',transactionid=transaction_id)
#         order.status = 'Placed'
#         order.complete=True
        
#         order.save()

        
#         try:
#             if order.couponused.used==True:
#                 coupon_check = CouponUsed.objects.get(user = user,used = True,order = order)
#                 coupid=coupon_check.coupon
#                 coupon = CouponDetail.objects.get(id=coupid.id)
#                 print("old total........................",order.get_cart_oldtotal)
#                 lessed_money = (order.get_cart_oldtotal * coupon_check.coupon.percentage / 100)
#                 coupon.count = coupon.count + 1
#                 coupon.loss = coupon.loss +lessed_money
#                 coupon_check.loss=lessed_money
#                 coupon_check.applied=True
#                 order.coupon_used=True
#                 coupon.save()
#                 coupon_check.save()
#                 order.save()
#             else:
#                 print("couponused isnt true!!!!!!!!!!!!!!!!!!!!!!!!!!!")
#         except:
#             print("Error")


#         return JsonResponse({'status': 'Your order has been Placed Successfully'})



    



# @never_cache
# def proceed(request):
#     print('hello')
#     if request.method == 'POST':
#         payment = request.POST.get('payment')
#         address_id = request.POST.get('address')
#         print(address_id)
#         status = True if str(payment) != 'COD' else False
#         address = Address.objects.get(id=address_id)
#         print('hrrrr1')
#         user = request.user
#         print(request.user)
#         order = Order.objects.get(user=user,order_status=False)
#         items = order.orderitem_set.all()
#         quantity_status = True
#         outOfStock = []
#         available = []
#         for item in items:
#             if item.quantity > item.product.stock:
#                 quantity_status = False
#                 outOfStock.append(str(item.product.id))
#                 available.append(str(item.product.stock))
#         if quantity_status is True:
#             Order.objects.filter(user=user,order_status=False).update(order_status=True, address=address, payment=status)
#             response = {'status':'success'}
#         else:
#             response = {'status':'error','outOfStock':outOfStock,'available':available}
#         return JsonResponse(response)
#     return redirect('home')



#the back up original

# @never_cache
# @csrf_exempt
# def proceed(request):
#     print('michu/////////////////////')
#     if request.method == 'POST':
#         payment = request.POST.get('payment')
#         print('this is payment/////////////////',payment)
#         address_id = request.POST.get('address')
#         coupen_type = request.POST.get('coupen')[4:]
#         coupen_id = request.POST.get('coupen')[:4]

#         status = True if str(payment) != 'COD' else False
#         print('hrrrbef1')
#         print(request.user)
#         address = Address.objects.get(id=address_id)
#         user = request.user
#         print('hrrrbef2')
#         try:
#             order = Order.objects.get(user=user,order_status=False,buyNow=True) #buy now should be changed if condition
#         except:
#             order = Order.objects.get(user=user,order_status=False,buyNow=False)
#         print('this is order of the current one',order)
#         print(order.id)
#         items = order.orderitem_set.all()
#         quantity_status = True
#         outOfStock = []
#         available = []
#         for item in items:
#             if item.quantity > item.product.stock:
#                 quantity_status = False
#                 outOfStock.append(str(item.product.id))
#                 available.append(str(item.product.stock))
#         if quantity_status is True:
#             if order.buyNow==True:
#                 Order.objects.filter(user=user,order_status=False,buyNow=True).update(order_status=True, address=address)
#                 if coupen_type == 'scpn':
#                     SignupCoupon.objects.filter(id=coupen_id).update(proceed=True) #
#                 elif coupen_type == 'cupn':
#                     coupen = Coupen.objects.filter(id=coupen_id)
#                     print(coupen)
#                     getCoupen = coupen.get(id=coupen_id)
#                     coupen.update(remaining=int(getCoupen.remaining)-1)
#             else:
#                 print('.........before order')
#                 check=Order.objects.filter(user=user,order_status=False,buyNow=False).update(order_status=True, address=address)
#                 if coupen_type == 'scpn':
#                     SignupCoupon.objects.filter(id=coupen_id).update(proceed=True) #
#                 elif coupen_type == 'cupn':
#                     coupen = Coupen.objects.filter(id=coupen_id)
#                     print(coupen)
#                     getCoupen = coupen.get(id=coupen_id)
#                     coupen.update(remaining=int(getCoupen.remaining)-1)
#                 print('...........is ',check)
#             # Order.objects.filter(user=user,order_status=False).update(order_status=True, address=address, payment=status)
#             transaction_id = order.id
#             total_amount=order.get_cart_total
#             print('this is total amount///////////',total_amount)
#             Payments.objects.get_or_create(order = order,payment_method = 'COD',total_amount = total_amount, status = 'Completed' ,transaction_id=transaction_id) # take a look at this line it is too suspicious and it is michu code here payment status is true but for michu is completed
#             # Pay.objects.get_or_create(order = order,method = 'COD',amount = total_amount,status = 'Completed',transactionid=transaction_id)
#             for item in items :
#                 ordered = item.quantity
#                 prestocks = item.product.stock
#                 poststocks = prestocks - ordered
#                 productid = item.product.id
#                 Product.objects.filter(id = productid).update(stock = poststocks)
#             response = {'status':'success','orderId':order.id}
#         else:
#             response = {'status':'error','outOfStock':outOfStock,'available':available}
#         return JsonResponse(response)
#     return redirect('home')



@never_cache
@csrf_exempt
def proceed(request):
    print('michu/////////////////////')
    if request.method == 'POST':
        payment = request.POST.get('payment')
        print('this is payment/////////////////',payment)
        address_id = request.POST.get('address')
        coupen_type = request.POST.get('coupen')[4:]
        coupen_id = request.POST.get('coupen')[:4]
        print('...........this is the payment',payment)
        status = True if str(payment) == 'razorpay' else False
        print('hrrrbef1')
        print(request.user)
        address = Address.objects.get(id=address_id)
        user = request.user
        print('hrrrbef2')
        try:
            order = Order.objects.get(user=user,order_status=False,buyNow=True) #buy now should be changed if condition
        except:
            order = Order.objects.get(user=user,order_status=False,buyNow=False)
        print('this is order of the current one',order)
        print(order.id)
        items = order.orderitem_set.all()
        quantity_status = True
        outOfStock = []
        available = []
        for item in items:
            if item.quantity > item.product.stock:
                quantity_status = False
                outOfStock.append(str(item.product.id))
                available.append(str(item.product.stock))
        if quantity_status is True:
            if order.buyNow==True:
                Order.objects.filter(user=user,order_status=False,buyNow=True).update(order_status=True, address=address)
                if coupen_type == 'scpn':
                    SignupCoupon.objects.filter(id=coupen_id).update(proceed=True) #
                elif coupen_type == 'cupn':
                    coupen = Coupen.objects.filter(id=coupen_id)
                    print(coupen)
                    getCoupen = coupen.get(id=coupen_id)
                    coupen.update(remaining=int(getCoupen.remaining)-1)
            else:
                print('.........before order')
                check=Order.objects.filter(user=user,order_status=False,buyNow=False).update(order_status=True, address=address)
                if coupen_type == 'scpn':
                    SignupCoupon.objects.filter(id=coupen_id).update(proceed=True) #
                elif coupen_type == 'cupn':
                    coupen = Coupen.objects.filter(id=coupen_id)
                    print(coupen)
                    getCoupen = coupen.get(id=coupen_id)
                    coupen.update(remaining=int(getCoupen.remaining)-1)
                print('...........is ',check)
            # Order.objects.filter(user=user,order_status=False).update(order_status=True, address=address, payment=status)
            transaction_id = order.id
            total_amount=order.get_cart_total
            print('this is total amount///////////',total_amount)
            if status == True:
                print('/////////////////////////  razorpay')
                Payments.objects.get_or_create(order = order,payment_method = 'razorpay',total_amount = total_amount, status = 'Completed' ,transaction_id=transaction_id) # take a look at this line it is too suspicious and it is michu code here payment status is true but for michu is completed
            else:
                print('////////////////////////   COD')
                Payments.objects.get_or_create(order = order,payment_method = 'COD',total_amount = total_amount, status = 'Completed' ,transaction_id=transaction_id) # take a look at this line it is too suspicious and it is michu code here payment status is true but for michu is completed
            # Pay.objects.get_or_create(order = order,method = 'COD',amount = total_amount,status = 'Completed',transactionid=transaction_id)
            for item in items :
                ordered = item.quantity
                prestocks = item.product.stock
                poststocks = prestocks - ordered
                productid = item.product.id
                Product.objects.filter(id = productid).update(stock = poststocks)
            response = {'status':'success','orderId':order.id}
        else:
            response = {'status':'error','outOfStock':outOfStock,'available':available}
        return JsonResponse(response)
    return redirect('home')








# def proceedwifi(request):
#     if request.method == 'POST':
        
#         payment = request.POST.get('payment')
#         address_id = request.POST.get('address')
#         coupen_typee = request.POST.get('coupen')
#         print(coupen_typee)
#         coupen_type = request.POST.get('coupen')[:4]
#         coupen_id = request.POST.get('coupen')[4:]
#         status = True if str(payment) != 'COD' else False
#         address = Address.objects.get(id=address_id)
#         user = request.user
#         try:
#             order = Order.objects.get(user=user,order_status=False,buyNow=True)
#         except:
#             order = Order.objects.get(user=user,order_status=False,buyNow=False)
#         items = order.orderitem_set.all()
#         quantity_status = True
#         outOfStock = []
#         available = []
#         for item in items:
#             if item.quantity > item.product.stock:
#                 quantity_status = False
#                 outOfStock.append(str(item.product.id))
#                 available.append(str(item.product.stock))
#         if quantity_status is True:
#             if order.buyNow == True:
#                 Order.objects.filter(user=user,order_status=False,buyNow=True).update(order_status=True, address=address, payments.payment_status=status, payments__payment_method=payment, payments__total_amount=order.get_cart_total)
#                 if coupen_type == 'scpn':
#                     SignupCoupon.objects.filter(id=coupen_id).update(proceed=True) #
#                 elif coupen_type == 'cupn':
#                     coupen = Coupen.objects.filter(id=coupen_id)
#                     print(coupen)
#                     getCoupen = coupen.get(id=coupen_id)
#                     coupen.update(remaining=int(getCoupen.remaining)-1) #
#             else:
#                 Order.objects.filter(user=user,order_status=False,buyNow=False).update(order_status=True, address=address,  payments__payment_status=status, payments__payment_method=payment, payments__total_amount=order.get_cart_total)
#                 if coupen_type == 'scpn':
#                     SignupCoupon.objects.filter(id=coupen_id).update(proceed=True) #
#                 elif coupen_type == 'cupn':
#                     coupen = Coupen.objects.filter(id=coupen_id)
#                     print(coupen)
#                     getCoupen = coupen.get(id=coupen_id)
#                     coupen.update(remaining=int(getCoupen.remaining)-1) #
#             for item in items :
#                 ordered = item.quantity
#                 prestocks = item.product.stock
#                 poststocks = prestocks - ordered
#                 productid = item.product.id
#                 Product.objects.filter(id = productid).update(stock = poststocks)
#             response = {'status':'success','orderId':order.id}
#         else:
#             response = {'status':'error','outOfStock':outOfStock,'available':available}
#         return JsonResponse(response)
#     return redirect('home')




# salmufunc
# @ csrf_exempt
# @login_required(login_url='signin')
# def order_by_paypal(request):
    
#     if request.method == 'POST':        
#         customer = request.user
#         order, created = Order.objects.get_or_create(user = customer,status = 'New')
#         items = order.orderitem_set.all()
#         for item in items :
#             ordered_items = item.quantity
#             current_stock = item.product.stock
#             new_stock = current_stock - ordered_items
#             product_id = item.product.id
#             Product.objects.filter(id = product_id).update(stock = new_stock)
#         total_amount = order.get_cart_total
#         transaction_id = request.POST.get('order_id')
#         Payments.objects.get_or_create(order = order,payment_method = 'Paypal',total_amount = total_amount,payment_status = True, transaction_id = transaction_id)
#         order.date_order = datetime.date.today()
#         order.status = 'Pending'
#         order.save()
#         return JsonResponse({'status': 'Your order has been Placed Successfully'})


#michfunc the current working model
@csrf_exempt
def order_by_paypal(request):
    if request.method == 'POST':      
        user = request.user
        try:
            order= Order.objects.get(user = user,order_status=False,buyNow=False)
        except:
            order= Order.objects.get(user = user,order_status=False,buyNow=True)
        items = order.orderitem_set.all()
        for item in items :
            ordered = item.quantity
            prestocks = item.product.stock
            poststocks = prestocks - ordered
            productid = item.product.id
            Product.objects.filter(id = productid).update(stock = poststocks)
        total_amount = order.get_cart_total
        transactionid = order.id
        Payments.objects.get_or_create(order = order,payment_method = 'Paypal',total_amount = total_amount,status = 'Completed', transaction_id = transactionid)
        order.status = 'Placed'
        order.order_status=True
        order.complete=True
        order.save()
        return JsonResponse({'status': 'Your order has been Placed Successfully'})









@never_cache
@login_required(login_url='/adminlogin')
def admin_home(request):
    if request.user.is_authenticated:
        products = Product.objects.all()
        placed = Order.objects.filter(status= 'Placed').count()
        shipped = Order.objects.filter(status= 'shipped').count()
        completed = Order.objects.filter(status= 'Completed').count()
        cancelled = Order.objects.filter(status= 'Cancelled').count()
        out_of_delivery = Order.objects.filter(status= 'Out Of Delevery').count()
        returned = Order.objects.filter(status= 'Return').count()
        order_status = [placed,shipped,out_of_delivery,completed,cancelled,returned]
        cod = Payments.objects.filter(payment_method = 'COD').count()
        paypal = Payments.objects.filter(payment_method = 'Paypal').count()
        razorpay = Payments.objects.filter(payment_method = 'razorpay').count()
        payment_type = [cod,paypal,razorpay]
        orderitems = OrderItem.objects.filter(order= completed)
        customers = User.objects.all().count()
        orders = Order.objects.all().count()
        product_count = Product.objects.all().count()
        total_revenue = Payments.objects.all().aggregate(Sum('total_amount'))
        context = {'products':products,'order_status': order_status, 'payment_type': payment_type, 
        'customers':customers,'orders': orders, 'product_count':product_count,'total_revenue':total_revenue}
        return render(request,'admin2.html',context)
    else:
        return redirect('adminlogin')


@never_cache
# @login_required(login_url='/iamadmin')
def adminorder(request):
    # orderdetails = Order.objects.all().exclude(order_status='Cart').order_by('-id')
    orderdetails = Order.objects.all().order_by('-id')

    context = {'orderdetails' : orderdetails }
    
    return render(request,'adminorders.html',context)





# @login_required(login_url='/iamadmin')
def adminorders_view(request, id):
    order, created = Order.objects.get_or_create(id = id)
    items = order.orderitem_set.all()
    context = { 'order':order , 'items': items, }
    return render(request,'adminorders_view.html', context)


# @login_required(login_url='/iamadmin')
def adminorderupdate(request,id):
    order = Order.objects.get(id = id)
    context = {'order': order}
    return render(request,'adminorderupdate.html',context)
    




# @login_required(login_url='/iamadmin')
def adminorder_cancel(request, id):
    order = Order.objects.get(id = id)
    items = OrderItem.objects.filter(order = order)
    order.order_status = False
    for item in items :
            ordered_items = item.quantity
            current_stock = item.product.stock
            new_stock = current_stock + ordered_items
            product_id = item.product.id
            Product.objects.filter(id = product_id).update(stock = new_stock)
    order.save()
    return redirect('adminorder')



# @login_required(login_url='/iamadmin')
def order_shipped(request, id):
    order = Order.objects.get(id = id)
    updated = 'shipped'
    # order.order_status = updated
    order.status = updated
    order.save()
    return redirect ('adminorder')

# @login_required(login_url='/iamadmin')
def order_ood(request, id):
    order = Order.objects.get(id = id)
    updated = 'Out Of Delevery'
    # order.order_status = updated
    order.status = updated
    order.save()
    return redirect ('adminorder')


#MUST LOOK DEEPLY IN THIS FUNCTION
# @login_required(login_url='/iamadmin')
def order_completed(request, id):
    order = Order.objects.get(id = id)
    # form = OrderUpdation()   #MUST LOOK DEEPLY IN THIS FUNCTION
    updated = 'Completed'    
    payobj = Payments.objects.get(order = order)
    transaction_id = datetime.datetime.now().timestamp()
    payobj.transaction_id = transaction_id
    # payobj.payment_status = 'Completed'
    payobj.payment_status = True
    payobj.status = 'Completed'
    payobj.save()
    # order.order_status = updated
    order.order_status = True
    order.status = updated
    order.save()
    return redirect ('adminorder')


# @never_cache
# @login_required(login_url='/iamadmin')
def categories_add(request):
    form = Categories_form()
    if request.method == 'POST' :
        Category.objects.create(name=request.POST.get('name'))
        return redirect('category_management')
    context = {'form' : form}
    return render(request, 'category_form.html', context)



# @login_required(login_url='/iamadmin')
def categories_update(request,id):
    form = Categories_form()
    if request.method == 'POST' :
        i = Category.objects.get(pk = id)
        form = Categories_form(request.POST, instance = i)
        if form.is_valid():
            form.save()
        return redirect('category_management')
    else :
        i= Category.objects.get(pk = id)
        form = Categories_form( instance = i)
    context = {'form' : form}
    return render(request, 'category_form.html', context)


# @login_required(login_url='/iamadmin')
def categories_delete(request,id):
    print('...........delete is working')
    # id  = request.GET.get('id')
    id = id
    i = Category.objects.get(id = id)
    i.delete()
    context = {'categories' : Category.objects.all()}
    return render(request,'category_management.html',context)



def category_management(request):
    context = {'categories' : Category.objects.all()}
    return render(request,'category_management.html',context)


# def adminsale(request):
#     orderdetails = Order.objects.all().order_by('-id')

#     context = {'orderdetails' : orderdetails }
    
#     return render(request,'adminsale2.html',context)



def usercancelorder(request, id):
    print('..........cancel')
    order = Order.objects.get(id = id)
    print('..........orderid',order)
    items = OrderItem.objects.filter(order = order)
    print('..........items',items)
    order.status = 'Cancelled'
    print('..........order status',order.status)
    for item in items :
        ordered = item.quantity
        stock = item.quantity
        newstock = stock + ordered
        productid = item.product.id
        Product.objects.filter(id = productid).update(stock = newstock)
    order.save()
    return redirect('user_order')
    


def user_invoice(request,id):
    user = request.user
    order = Order.objects.get(id=id)
    items=order.orderitem_set.all()
    context={'order':order,'items':items}
    return render (request, "user_invoice.html",context)


# @never_cache
# @login_required(login_url='/iamadmin/')
# def adminsale(request):
#     page = 'salesreport'
#     global order_data
#     order_data = OrderItem.objects.filter(order__payments__status='Completed')
#     yr = []
#     ag = 2000
#     for i in range(0,51):
#         yr.append(ag + i)
#     if request.method == 'POST':
#         from_date = request.POST.get('from_date')
#         to_date = request.POST.get('to_date')
#         year = request.POST.get('year')
#         month = request.POST.get('month')
#         m = month[6:]
#         if from_date != '' and to_date != '' :
#             order_data = OrderItem.objects.filter(order__date__range=[from_date,to_date]).filter(order__payments__status='Completed').order_by('order_date')
#         elif  month != '' :
#             order_data = OrderItem.objects.filter(order__date__month=m).filter(order__payments__status='Completed').order_by('order_date')
#         elif  year != '' :
#             order_data = OrderItem.objects.filter(order__date__year=year).filter(order__payments__status='Completed').order_by('order_date')
#     context = {'order_data': order_data, 'years': yr,'page': page,}
#     return render(request,'adminsale3.html', context)



@never_cache
@login_required(login_url='/iamadmin/')
def adminsale(request):
    page = 'salesreport'
    global order_data
    order_data = OrderItem.objects.filter(order__payments__status='Completed')
    yr = []
    ag = 2000
    months = ['January', 'February', 'March','April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    for i in range(0,51):
        yr.append(ag + i)
    if request.method == 'POST':
        datestr = request.POST.get('dates')
        print('this is datestr',datestr)
            #start date
        mo = datestr[:2]
        da = datestr[3:5]
        ye = datestr[6:10]
        #enddate
        mo1 = datestr[13:15]
        da1 = datestr[16:18]
        ye1 = datestr[19:]
        from_date = ye+'-'+mo+'-'+da
        to_date = ye1+'-'+mo1+'-'+da1
        print('this is to date',to_date)
        
        year = request.POST.get('year')
        month = request.POST.get('month')
        print('this is month',month)
        m = month
        print('this is second month',m)
        print('this is from date',from_date)
        if  month != '' :
            order_data = OrderItem.objects.filter(order__date_order__month=m).filter(order__payments__status='Completed').order_by('order__date_order')
        elif  year != '' :
            order_data = OrderItem.objects.filter(order__date_order__year=year).filter(order__payments__status='Completed').order_by('order__date_order')
        elif from_date != '' and to_date != '' :
            order_data = OrderItem.objects.filter(order__date_order__range=[from_date,to_date]).filter(order__payments__status='Completed').order_by('order__date_order')

    context = {'order_data': order_data, 'years': yr,'page': page,'months':months}
    return render(request,'adminsale3.html', context)











@never_cache
def export_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=SalesReport'+str(datetime.datetime.now())+'.csv'
    writer = csv.writer(response)   
    writer.writerow(['User Id','Name','Number Of Products','Order Date','Amount','Payment Type'])
    # order_data = OrderItem.objects.filter(order__payments__status='Completed')
    for data in order_data:
        writer.writerow([data.order.user.id, data.order.user, data.order.get_cart_items, data.order.date_order,data.order.payments.total_amount , data.order.payments.payment_method])
    return response


@never_cache
def export_excel(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=SalesReport'+str(datetime.datetime.now())+'.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Sales Report')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['User Id','Name','Order Date','Amount','Payment Type']
    # order_data = Order.objects.filter(payments__status='Completed')
    

    for col_num in range(len(columns)):
        ws.write(row_num,col_num,columns[col_num],font_style)

    font_style = xlwt.XFStyle()
    print('this is order data',order_data)
    rows = order_data.values_list(
        # 'id','order_customer','order_date','payment_total_amount','payment_payment_method'
        'id','user__username','date_order','payments__total_amount','payments__payment_method'
    )
    

    for row in rows:
        row_num = row_num + 1

        for col_num in range(len(columns)):
             ws.write(row_num,col_num,str(row[col_num]),font_style)
    wb.save(response)

    return response





# @never_cache
# def export_excel(request):
#     page = 'salesreport'
#     global order_data
#     order_data = OrderItem.objects.filter(order__payments__status='Completed')
#     yr = []
#     ag = 2000
#     months = ['January', 'February', 'March','April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
#     for i in range(0,51):
#         yr.append(ag + i)
#     if request.method == 'POST':
#         datestr = request.POST.get('dates')
#         print('this is datestr',datestr)
#             #start date
#         mo = datestr[:2]
#         da = datestr[3:5]
#         ye = datestr[6:10]
#         #enddate
#         mo1 = datestr[13:15]
#         da1 = datestr[16:18]
#         ye1 = datestr[19:]
#         from_date = ye+'-'+mo+'-'+da
#         to_date = ye1+'-'+mo1+'-'+da1
#         print('this is to date',to_date)
        
#         year = request.POST.get('year')
#         month = request.POST.get('month')
#         print('this is month',month)
#         m = month
#         print('this is second month',m)
#         print('this is from date',from_date)
#         if  month != '' :
#             order_data = OrderItem.objects.filter(order__date_order__month=m).filter(order__payments__status='Completed').order_by('order__date_order')
#         elif  year != '' :
#             order_data = OrderItem.objects.filter(order__date_order__year=year).filter(order__payments__status='Completed').order_by('order__date_order')
#         elif from_date != '' and to_date != '' :
#             order_data = OrderItem.objects.filter(order__date_order__range=[from_date,to_date]).filter(order__payments__status='Completed').order_by('order__date_order')

#     context = {'order_data': order_data, 'years': yr,'page': page,'months':months}



#     print('this is order data ok',order_data)

#     response = HttpResponse(content_type='application/ms-excel')
#     response['Content-Disposition'] = 'attachment; filename=SalesReport'+str(datetime.datetime.now())+'.xls'
#     wb = xlwt.Workbook(encoding='utf-8')
#     ws = wb.add_sheet('Sales Report')
#     row_num = 0
#     font_style = xlwt.XFStyle()
#     font_style.font.bold = True
#     columns = ['User Id','Name','Order Date','Amount','Payment Type']
#     # order_data = Order.objects.filter(payments__status='Completed')
    

#     for col_num in range(len(columns)):
#         ws.write(row_num,col_num,columns[col_num],font_style)

#     font_style = xlwt.XFStyle()
#     print('this is order data',order_data)
#     rows = order_data.values_list(
#         # 'id','order_customer','order_date','payment_total_amount','payment_payment_method'
#         # 'id','user__username','date_order','payments__total_amount','payments__payment_method'
#         'id','date_added','order','order_id','quantity'
#     )
    

#     for row in rows:
#         row_num = row_num + 1

#         for col_num in range(len(columns)):
#              ws.write(row_num,col_num,str(row[col_num]),font_style)
#     wb.save(response)

#     return response



# user side coupon

def coupon(request):
    if request.method == "POST":
        coupenId = request.POST.get('coupenId')[4:]
        coupenType = request.POST.get('coupenId')[:4]
        orderId = request.POST.get('orderId')
        action = request.POST.get('action')
        if coupenType == 'scpn':
            coupen = SignupCoupon.objects.get(id=coupenId)
        else: 
            coupenType == 'cupn'
            coupen = Coupen.objects.get(id=coupenId)  # this is the object which contain the name,price,and other details look in models for further details
        if action == 'apply':
            Order.objects.filter(id=orderId).update(coupen=int(coupen.price[:-1]))  # this coupen.price is basically used to get the value 25 from the code 25% which we get from the coupen that is applied
            if coupenType == 'scpn':
                coupen = SignupCoupon.objects.filter(id=coupenId)
                coupen.update(available = False)
        else:
            Order.objects.filter(id=orderId).update(coupen=None)
            if coupenType == 'scpn':
                coupen = SignupCoupon.objects.filter(id=coupenId)
                coupen.update(available = True)
        order = Order.objects.get(id=orderId)
        return JsonResponse({'total':order.get_cart_total})


# admin side coupon

def coupon_manage(request):
    coupens = Coupen.objects.all()
    return render(request, 'admincoupons.html',{'coupons':coupens})

def cpn_add(request):
    if request.method == "POST":
        name = request.POST.get('name')
        offer = request.POST.get('offer')
        stock = request.POST.get('stock')
        Coupen.objects.create(name = name, price = offer, remaining = stock)
    return redirect('coupon_manage')

def cpn_edit(request):
    if request.method == "POST":
        id = request.POST.get('typeId')
        val = request.POST.get('val')
        bal = request.POST.get('bal')
        name = request.POST.get('name')
        Coupen.objects.filter(id = id).update(price=val, name=name, remaining=bal)
    return redirect('coupon_manage')


def cpn_dlt(request,id):
    Coupen.objects.filter(id=id).delete()
    return redirect('coupon_manage')




def add_offer(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        brand_id = request.POST.get('brand')
        product_id = request.POST.get('product')
        offer = request.POST.get('offer')
        if name == 'Category':
            offerId = Offer.objects.create(name='Category',price=offer)
            Category.objects.filter(id=brand_id).update(category_off=offerId)
        elif name == 'Product':
            offerId = Offer.objects.create(name='Product',price=offer)
            Product.objects.filter(id=product_id).update(product_off=offerId)
    return redirect('offer_management')

def delete_Offer(request,id):
    Offer.objects.filter(id=id).delete()
    return redirect('offer_management')

def offers(request):
    if request.method == "POST":
        print('juy')
        id = request.POST.get('typeId')
        val = request.POST.get('val')
        Offer.objects.filter(id=id).update(price=val)
    return redirect('offer_management')


def offer_mangement(request):
    products = Product.objects.all()
    brands = Category.objects.all()
    off_products = Product.objects.exclude(product_off=None )
    off_brands = Category.objects.exclude(category_off=None )
    for brand in off_brands:
        brand.items = products.filter(brand=brand).count()
    return render(request, 'adminoffer.html',{'off_products':off_products,'off_brands':off_brands,'products':products,'brands':brands})













