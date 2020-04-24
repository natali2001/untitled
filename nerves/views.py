from django.shortcuts import render
from .forms import SubscriberForm
from products.models import *



def nerves(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_nerves = products_images.filter(product__category__id=2)
    return render(request, 'landing/nerves.html', locals())



