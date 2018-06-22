from django.shortcuts import render,redirect
from django.conf import settings
from .models import Cart
from categoryApp.models import Product
# Create your views here.
User = settings.AUTH_USER_MODEL
def cartHome(request):
    cart_obj, new_obj=Cart.objects.newCart_or_getCart(request)
    #print(cart_id)
    #request.session['cart_id']=12 #Setter
    #print(request.session)
    #key=request.session.session_key #Primary Key
    #print(key)
    #request.session['user']=request.user.username
    #print(request.session.get('user'))
    return render(request,"cart/cart_home.html",{'cart':cart_obj})


def cartUpdate(request):
    #print(request.POST)
    product_id=request.POST.get('product_id')
    if product_id is not None:
        try:
            product_obj=Product.objects.get(id=product_id)
        except:
            return redirect('cart:cartHome')
        cart_obj,new_obj=Cart.objects.newCart_or_getCart(request)
        print(product_obj)
        if product_obj in cart_obj.products.all():
            cart_obj.products.remove(product_obj)
        else:
            cart_obj.products.add(product_obj)
    #print(cart_obj.products.all())
    return redirect('cart:cartHome')
