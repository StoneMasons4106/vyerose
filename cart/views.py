from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from . import contexts
from .models import UserCart
import json

from products.models import Product

# Create your views here.

def view_cart(request):
    """ A view that renders the cart contents page """

    context = contexts.cart_contents(request)
    template = 'cart/cart.html'
    return render(request, template, context)


def add_to_cart(request, item_id):
    """ Add a quantity of the specified product to the shopping cart """
        
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    try:
        cart = get_object_or_404(UserCart, user=request.user)
        jsonready_cart = cart.cart.replace("'", '"')
        user_cart = json.loads(jsonready_cart)

        if item_id in user_cart.keys():
            user_cart[item_id] += quantity
            cart.cart = user_cart
            cart.save()
            messages.success(request, f'Updated {product.name} quantity to {quantity}')
        else:
            user_cart[item_id] = quantity
            cart.cart = user_cart
            cart.save()
            messages.success(request, f'Added {product.name} to your cart')
    
    except:
        user_cart = {}

        user_cart[item_id] = quantity
        cart = UserCart(user=request.user)
        cart.cart = user_cart
        cart.save()
        messages.success(request, f'Added {product.name} to your cart')


    request.session['cart'] = cart.cart
    return redirect(redirect_url)
    

def adjust_cart(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    cart = get_object_or_404(UserCart, user=request.user)
    
    if quantity > 0:
        jsonready_cart = cart.cart.replace("'", '"')
        json_cart = json.loads(jsonready_cart)
        json_cart[item_id] = quantity
        cart.cart = json_cart
        cart.save()
        messages.success(request, f'Updated {product.name} quantity to {quantity}')
    else:
        json_cart = cart.cart.replace("'", '"')
        json.loads(json_cart).pop(item_id)
        cart.cart = json_cart
        cart.save()
        messages.success(request, f'Removed {product.name} from your cart')

    request.session['cart'] = json_cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """Remove the item from the shopping cart"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        cart = get_object_or_404(UserCart, user=request.user)

        json_cart = cart.cart.replace("'", '"')
        json.loads(json_cart).pop(item_id)
        cart.cart = json_cart
        cart.save()
        messages.success(request, f'Removed {product.name} from your cart')

        request.session['cart'] = json_cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)