from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product, Category
from .models import UserCart
import json

def cart_contents(request):

    cart_items = []
    total = 0
    product_count = 0
    try:
        cart = get_object_or_404(UserCart, user=request.user)
        jsonready_cart = cart.cart.replace("'", '"')
        user_cart = json.loads(jsonready_cart)
    except:
        user_cart = request.session.get('cart', {})

    for item_id, item_data in user_cart.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            total += item_data * product.price
            product_count += item_data
            cart_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })
        else:
            product = get_object_or_404(Product, pk=item_id)
            for quantity in item_data.items():
                total += quantity * product.price
                product_count += quantity
                cart_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                })
    
    delivery = total / 10
    grand_total = total + delivery
    categories = Category.objects.values()
    
    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'grand_total': grand_total,
        'categories': categories,
    }

    return context