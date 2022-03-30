from dataclasses import field
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

class MyProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields ='__all__'


    def __init__(self, *args, **kwargs):
        super(MyProductForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control border border-success py-1 text-dark', 'placeholder':'Name', 'id':'name'})
        self.fields['brand'].widget.attrs.update({'class': 'form-control border border-success py-1 text-dark', 'placeholder':'brand', 'id':'name'})
        self.fields['storage'].widget.attrs.update({'class': 'form-control border border-success py-1 text-dark', 'placeholder':'storage', 'id':'name'})
        self.fields['RAM'].widget.attrs.update({'class': 'form-control border border-success py-1 text-dark', 'placeholder':'RAM', 'id':'name'})
        self.fields['display'].widget.attrs.update({'class': 'form-control border border-success py-1 text-dark', 'placeholder':'display', 'id':'name'})
        self.fields['processor'].widget.attrs.update({'class': 'form-control border border-success py-1 text-dark', 'placeholder':'processor', 'id':'name'})
        self.fields['OS'].widget.attrs.update({'class': 'form-control border border-success py-1 text-dark', 'placeholder':'OS', 'id':'name'})
        self.fields['battery'].widget.attrs.update({'class': 'form-control border border-success py-1 text-dark', 'placeholder':'battery', 'id':'name'})
        self.fields['price'].widget.attrs.update({'class': 'form-control border border-success py-1 text-dark', 'placeholder':'price', 'id':'price', 'type':'number'})
        self.fields['image1'].widget.attrs.update({'class': 'form-control border border-success py-1 text-dark', 'placeholder':'image1', 'id':'image1', 'type' : 'file', 'accept' : "image/gif, image/jpeg, image/png, image/webp " })
        self.fields['image2'].widget.attrs.update({'class': 'form-control border border-success py-1 text-dark', 'placeholder':'image2', 'id':'image2' ,  'type' : 'file', 'accept' : "image/gif, image/jpeg, image/png, image/webp" })
        self.fields['image3'].widget.attrs.update({'class': 'form-control border border-success py-1 text-dark', 'placeholder':'image3', 'id':'image3' ,  'type' : 'file', 'accept' : "image/gif, image/jpeg, image/png, image/webp" })
        self.fields['image4'].widget.attrs.update({'class': 'form-control border border-success py-1 text-dark', 'placeholder':'image4', 'id':'image4' ,  'type' : 'file', 'accept' : "image/gif, image/jpeg, image/png, image/webp" })
        self.fields['stock'].widget.attrs.update({'class': 'form-control border border-success py-1 text-dark', 'placeholder':'stock', 'id':'stock'})
        self.fields['product_category'].widget.attrs.update({'class': 'form-control border border-success py-1 text-dark', 'placeholder':'image1', 'product category':'product_category'})




class MyAddressForm(forms.ModelForm):
    class Meta:
        model=Address
        fields='__all__'
        exclude = ['aname']

    
    def __init__(self, *args, **kwargs):
        super(MyAddressForm, self).__init__(*args, **kwargs)
        self.fields['fname'].widget.attrs.update({'class': 'form-control border border-success py-1 text-dark', 'placeholder':'first name', 'id':'name'})
        self.fields['lname'].widget.attrs.update({'class': 'form-control border border-success py-1 text-dark', 'placeholder':'last name', 'id':'name'})
        self.fields['address'].widget.attrs.update({'class': 'form-control border border-success py-1 text-dark', 'placeholder':'address', 'id':'name'})
        self.fields['city'].widget.attrs.update({'class': 'form-control border border-success py-1 text-dark', 'placeholder':'city', 'id':'name'})
        self.fields['state'].widget.attrs.update({'class': 'form-control border border-success py-1 text-dark', 'placeholder':'state', 'id':'name'})
        self.fields['phone'].widget.attrs.update({'class': 'form-control border border-success py-1 text-dark', 'placeholder':'phone', 'id':'name'})
        self.fields['pincode'].widget.attrs.update({'class': 'form-control border border-success py-1 text-dark', 'placeholder':'pincode', 'id':'name'})
        

class MyUserFormUser(UserCreationForm):
    class Meta:
        model=User
        fields=('username','phone','email','password1','password2')
        
        
    def __init__(self,*args,**kwargs):
        super(MyUserFormUser, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control border border-success py-1 text-dark', 'placeholder':'username', 'id':'name'})
        self.fields['email'].widget.attrs.update({'class': 'form-control border border-success py-1 text-dark', 'placeholder':'email', 'id':'email'})
        self.fields['phone'].widget.attrs.update({'class': 'form-control border border-success py-1 text-dark', 'placeholder':'phone', 'id':'phone'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control border border-success py-1 text-dark', 'placeholder':'password', 'id':'password'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control border border-success py-1 text-dark', 'placeholder':'password', 'id':'password'})
        

class Categories_form(forms.ModelForm):
    
    class Meta :
        model = Category
        fields = '__all__'
        labels = {
            'category_name' : 'Category Name'

            
        }

    def __init__(self, *args, **kwargs):
        super(Categories_form, self).__init__(*args, **kwargs)
        self.fields['category_name'].widget.attrs.update({'class': 'form-control border border-danger py-1 text-dark', 'placeholder':'category_name', 'id':'category_name'})
    









#////////////////////////////////////////////////


# from cProfile import label
# from dataclasses import field
# from django import forms
# from userapp.models import *
# class Categories_form(forms.ModelForm):
    
#     class Meta :
#         model = Categorie
#         fields = ('category_name','category_img',)
#         labels = {
#             'category_name' : 'Category Name',
#             'category_img' : 'Banner Image'
            
#         }
#     def _init_(self, *args, **kwargs):
#         super(Categories_form, self)._init_(*args, **kwargs)

# class products_form(forms.ModelForm):
    
#     class Meta :
#         model = Product
#         fields = ('product_name','product_image','product_img_left',
#         'product_img_right', 'product_category', 'product_description',
#          'product_price','quantity_available', 'gender', 'new','offer',)
#         labels = {
#             'product_name' : 'Product Name',
#             'product_image' : 'Main Image',
#             'product_img_left' : 'Image 2',
#             'product_img_right' : 'Image 3',
#             'product_category' : 'Category',
#             'product_description': 'Product Description',
#             'product_price' : 'Price',
#             'quantity_available' : 'Available Quantity',
#             'gender' : 'Gender',
#             'new' : 'New',
#             'offer' : 'Offer',
#         }


#     def _init_(self, *args, **kwargs):
#         super(products_form, self)._init_(*args, **kwargs)


# class banner_form(forms.ModelForm):
    
#     class Meta :
#         model = Banner
#         fields = ('name','banner_image','header',
#         'description',)
#         labels = {
#             'name' : 'Banner Name',
#             'banner_image' : 'Banner Image',
#             'header' : 'Main Header',
#             'description' : 'Description',
           
#         }


#     def _init_(self, *args, **kwargs):
#         super(banner_form, self)._init_(*args, **kwargs)



# update_choices= [

#     ('Placed','Placed'),
#     ('Shipped', 'Shipped'),
#     ('Out Of Delivery','Out Of Delivery'),
#     ('Completed','Completed'),
#     ('Failed','Failed'),

# ]

# class OrderUpdation(forms.Form):

#     order_status = forms.CharField(
#         label='Select The Order Status', widget=forms.Select(choices=update_choices))

