from django.conf.urls import url
from categoryApp.models import Product
from .views import (
        SearchProductView
        )
app_name='search'
urlpatterns = [
    url(r'^$', SearchProductView.as_view(), name='list'),
]
