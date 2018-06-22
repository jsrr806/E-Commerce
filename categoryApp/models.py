import random
import os
from django.db import models
from django.db.models.signals import pre_save, post_save

from django.urls import reverse
from .utils import unique_slug_generator



class Product(models.Model):
    title           = models.CharField(max_length=120)
    company         = models.CharField(max_length=120,null=True)
    model           = models.CharField(max_length=200,unique=True,null=True)
    slug            = models.SlugField(blank=True, unique=True)
    description     = models.TextField()
    price           = models.DecimalField(decimal_places=2, max_digits=20, default=39.99)
    image           = models.ImageField(upload_to='image', null=True, blank=True)



    def get_absolute_url(self):
        #return "/category/{slug}/".format(slug=self.slug)
         return reverse("category:detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title


def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(product_pre_save_receiver, sender=Product)
