from django.shortcuts import render
from products.models import *


def vitamins(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_vitamin = products_images.filter(product__category__id=3)
    return render(request, 'landing/vitamins.html', locals())



