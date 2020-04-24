from django.shortcuts import render
from products.models import *


def antipyretic(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_cold = products_images.filter(product__category__id=1)
    return render(request, 'landing/category_product.html', locals())



