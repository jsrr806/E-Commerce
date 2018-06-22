from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save,post_save,m2m_changed
# Create your models here.
from categoryApp.models import Product
User = settings.AUTH_USER_MODEL

class CartManager(models.Manager):
    def newCart_or_getCart(self,request):
        new_obj=False
        cart_id=request.session.get("cart_id",None)
        active_cart = Cart.objects.filter(id=cart_id)
        if active_cart.count() == 1:
            print('Cart already Exist')
            cart_obj=active_cart.first()
            print(cart_obj.user)
            print(cart_id)
            if request.user.is_authenticated and cart_obj.user is None:
                cart_obj.user=request.user
                cart_obj.save()
        else:
            print('New Cart')
            print(request.user)
            user_obj=None
            new_obj=True
            if request.user.is_authenticated:
                user_obj=request.user
            cart_obj=Cart.objects.newCart(user=user_obj)
            request.session['cart_id']=cart_obj.id
        return cart_obj,new_obj

    def newCart(self, user=None):
        user_obj=None
        if user is not None:
            if user.is_authenticated:
                user_obj=user
                print(user)
        return self.model.objects.create(user=user_obj)

class Cart(models.Model):
    user = models.ForeignKey(User,null=True,blank=True,on_delete='cascade',related_name='user')#Any One can create his/her oen cart
    products = models.ManyToManyField(Product,blank=True)
    total = models.DecimalField(default=0.00,max_digits=10,decimal_places=2)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = CartManager()
    def __str__(self):
        return str(self.id)


def m2m_changed_cart_receiver(sender,instance,action,*args,**kwargs): #a signal to update total price in Cart
    if action =='post_add' or action =='post_remove' or action =='post_clear':
        products=instance.products.all()
        total=0
        for item in products:
            total+=item.price

        instance.total=total
        instance.save()

m2m_changed.connect(m2m_changed_cart_receiver,sender=Cart.products.through)
