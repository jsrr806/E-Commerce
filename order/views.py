from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .models import Order
from cart.models import Cart
from userApp.models import UserProfileInfo
# Create your views here.
def createOrder(request):
    if request.user.is_authenticated:
        cart_obj=Cart.objects.filter(user=request.user,active=True).first()
        print(cart_obj)
        order_obj=Order.objects.filter(cart=cart_obj).first()
        #print("hehehe")
        print(order_obj)
        user_info=UserProfileInfo.objects.filter(user=request.user).first()
        print(user_info)
        if order_obj is None:
            Order.objects.create(cart=cart_obj)
        return render(request,"order/checkout.html",{'cart_obj':cart_obj,'order_obj':order_obj,'user_info':user_info})
    else:
        return render(request, 'userApp/login.html', {'redirect_url':request.build_absolute_uri })

def setAddress(request):
    address=request.POST.get('address')
    print("papa")
    order_id=request.POST.get('order_id')
    print(order_id)
    order_obj=Order.objects.filter(order_id=order_id).first()
    order_obj.address=address
    print(request.POST.get('updateAddress'))
    order_obj.save()
    if request.POST.get('updateAddress') is not None:
        user_obj=UserProfileInfo.objects.filter(user=request.user).first()
        user_obj.address=order_obj.address
        user_obj.save()
    return render(request,'order/payment.html',{})
