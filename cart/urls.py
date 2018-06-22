from django.conf.urls import url

from .views import cartHome,cartUpdate

app_name='cart'
urlpatterns=[
    url(r'^$',cartHome,name='cartHome'),
    url(r'^update/$',cartUpdate,name='cartUpdate'),
]
