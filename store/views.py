import json

from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator
from django.http import JsonResponse


# Create your views here.
def main(request):
    context = {}
    return render(request, "store/main.html", context)


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()

    else:
        # Create empty cart for now for non-logged in user
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}

    context = {'items': items, 'order': order}
    return render(request, 'store/cart.html', context)


def store(request):
    products = Product.objects.all()
    paginator = Paginator(products, 2)  # Show 25 contacts per page.

    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)

    context = {
        'products': products
    }
    return render(request, "store/store.html", context)


def checkout(request):
    context = {}
    return render(request, "store/checkout.html", context)


def update_item(request):
    data = json.loads(request.body)
    product_id = data['productId']
    action = data['action']
    print('product_id: ', product_id)
    print('action: ', action)

    return JsonResponse("item was added", safe=False)
