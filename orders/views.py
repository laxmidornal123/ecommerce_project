import razorpay
import json
from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from cart.models import Cart
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from django.http import HttpResponse
from .models import Order
from .models import Order, OrderItem
from cart.models import Cart
from products.models import Review
from reportlab.platypus import Image
import os
@login_required
def checkout(request):
    cart = Cart.objects.get(user=request.user)
    items = cart.cartitem_set.all()

    total = 0
    for item in items:
        total += item.product.price * item.quantity

    amount = int(total * 100)

    client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

    payment = client.order.create({
        "amount": amount,
        "currency": "INR",
        "payment_capture": "1"
    })

    return render(request, "orders/payment.html", {
        "payment": payment,
        "total": total,
        "key": settings.RAZORPAY_KEY_ID
    })


@csrf_exempt
def verify_payment(request):
    if request.method == "POST":
        data = json.loads(request.body)
        return JsonResponse({'status': 'success'})


def order_success(request):
    return render(request, 'orders/success.html')


def track_order(request):
    return render(request, 'orders/track.html')
from django.shortcuts import get_object_or_404
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)
from reportlab.lib.styles import getSampleStyleSheet
from django.http import HttpResponse

def generate_invoice(request, order_id):

    order = get_object_or_404(Order, id=order_id)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="invoice_{order.id}.pdf"'

    doc = SimpleDocTemplate(response)
    styles = getSampleStyleSheet()

    content = []

    content.append(Paragraph("E-Commerce Invoice", styles['Title']))
    content.append(Spacer(1, 12))

    content.append(
        Paragraph(f"<b>Order ID:</b> {order.id}", styles['Normal'])
    )

    content.append(
        Paragraph(f"<b>Customer:</b> {order.user.username}", styles['Normal'])
    )

    content.append(
        Paragraph(
            f"<b>Order Date:</b> {order.created_at.strftime('%d-%m-%Y %H:%M')}",
            styles['Normal']
        )
    )

    content.append(
        Paragraph(
    f"<b>Total Amount:</b> Rs. {order.total_amount}",
    styles['Normal']
)
    )

    content.append(Spacer(1, 15))

    content.append(
        Paragraph("<b>Products Ordered:</b>", styles['Heading2'])
    )

    for item in order.items.all():

      content.append(
        Paragraph(
    f"{item.product.name} | Qty: {item.quantity} | Rs. {item.product.price}",
    styles['Normal']
)
    )

    if item.product.image:
        image_path = item.product.image.path

        if os.path.exists(image_path):
            product_image = Image(image_path, width=120, height=120)
            content.append(product_image)

    content.append(Spacer(1, 10))
    
    content.append(
        Paragraph(
            "Thank you for shopping with us!",
            styles['Heading3']
        )
    )

    doc.build(content)

    return response
@login_required
def order_history(request):
    orders = Order.objects.filter(
        user=request.user
    ).prefetch_related('items__product').order_by('-created_at')

    reviewed_products = Review.objects.filter(
        user=request.user
    ).values_list('product_id', flat=True)

    return render(request, 'orders/history.html', {
        'orders': orders,
        'reviewed_products': reviewed_products
    })
@login_required
def payment_success(request):
    cart = Cart.objects.get(user=request.user)
    items = cart.cartitem_set.all()

    total = 0
    for item in items:
        total += item.product.price * item.quantity

    # ✅ Create Order
    order = Order.objects.create(
        user=request.user,
        total_amount=total,
        address="Solapur"
    )

    # ✅ Save Order Items
    for item in items:
        OrderItem.objects.create(
            order=order,
            product=item.product,
            quantity=item.quantity
        )

    # ✅ Clear Cart
    items.delete()

    return render(request, 'orders/success.html', {'order': order})