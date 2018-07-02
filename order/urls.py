from django.conf.urls import url
from .views import createOrder,setAddress
app_name='order'

urlpatterns=[
    url(r'^create_order/$',createOrder,name='createOrder'),
    url(r'^deliver_to/$',setAddress,name='setAddress'),
]
