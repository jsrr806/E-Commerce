"""Ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

#from cart.views import cartHome
from .views import home_page
from userApp.views import user_logout
urlpatterns = [
    # url(r'^$', include('homeApp.urls')),
    #path('cart/',cartHome,name='cart'),
    url(r'^$', home_page,name='home'),
    path('admin/', admin.site.urls),
    url(r'cart/',include('cart.urls',namespace='cart')),
    url(r'category/',include('categoryApp.urls',namespace='category')),
    url(r'^userApp/',include('userApp.urls')),
    url(r'^order/',include('order.urls')),
    url(r'^logout/$',user_logout, name='logout'),
    url(r'^search/', include("search.urls", namespace='search')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
