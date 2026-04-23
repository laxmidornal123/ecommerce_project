from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Cart, CartItem
from products.models import Product
from django.shortcuts import redirect
# View Cart
@login_required
def cart_view(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    items = cart.cartitem_set.all()

    total = 0
    for item in items:
        total += item.product.price * item.quantity

    return render(request, 'cart/cart.html', {
        'items': items,
        'total': total
    })

# Add to Cart
@login_required
def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)

    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart')

# Increase Quantity
@login_required
def increase_quantity(request, item_id):
    item = CartItem.objects.get(id=item_id)
    item.quantity += 1
    item.save()
    return redirect('cart')

# Decrease Quantity
@login_required
def decrease_quantity(request, item_id):
    item = CartItem.objects.get(id=item_id)
    if item.quantity > 1:
        item.quantity -= 1
        item.save()
    return redirect('cart')
def remove_from_cart(request, product_id):
    cart = Cart.objects.get(user=request.user)
    product = Product.objects.get(id=product_id)

    item = CartItem.objects.filter(cart=cart, product=product).first()

    if item:
        item.delete()

    return redirect('cart')