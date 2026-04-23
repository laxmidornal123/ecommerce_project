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

def generate_invoice(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="invoice.pdf"'

    doc = SimpleDocTemplate(response)
    styles = getSampleStyleSheet()

    content = []

    content.append(Paragraph("Order Invoice", styles['Title']))
    content.append(Paragraph("Thank you for your purchase!", styles['Normal']))
    content.append(Paragraph("Amount Paid: ₹199", styles['Normal']))

    doc.build(content)

    return response
@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'orders/history.html', {'orders': orders})
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