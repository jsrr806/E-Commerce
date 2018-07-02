from django.db import models
from cart.models import Cart
from categoryApp.utils import unique_order_id_generator
from django.db.models.signals import pre_save,post_save
# Create your models here.
ORDER_STATUS_CHOICES = (
    ('created', 'Created'),
    ('paid', 'Paid'),
    ('shipped', 'Shipped'),
)
class Order(models.Model):
    order_id = models.CharField(max_length=120,blank=True)
    cart = models.OneToOneField(Cart,on_delete=models.CASCADE,null=True,blank=True)
    status = models.CharField(max_length=120,default='created',choices=ORDER_STATUS_CHOICES)
    total = models.DecimalField(default=0.00,max_digits=100,decimal_places=2)
    address = models.CharField(max_length=120,blank=True)

    def __str__(self):
        return self.order_id

    def update_total(self):
        cart_total=self.cart.total
        self.total=cart_total
        self.save()
        return cart_total

def pre_save_create_order_id(sender,instance,*args,**kwargs):
    if not instance.order_id:
        instance.order_id = unique_order_id_generator(instance)

pre_save.connect(pre_save_create_order_id,sender=Order)

def post_save_order(sender,instance,created,*args,**kwargs):
    if created:
        instance.total=instance.update_total()
        instance.save()
        #print("ch")
        print(instance.total)

post_save.connect(post_save_order,sender=Order)

def post_save_cart_total(sender,instance,created,*args,**kwargs):
    if not created:
        #print("f")
        print(instance.id)
        qs=Order.objects.filter(cart__id=instance.id)
        if qs.count()==1:
            qs.first().update_total()
            qs.first().save()

post_save.connect(post_save_cart_total,sender=Cart)
