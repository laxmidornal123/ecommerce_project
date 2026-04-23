from django.urls import path
from .views import checkout, payment_success, verify_payment, track_order, generate_invoice, order_history

urlpatterns = [
    path('', checkout, name='checkout'),

    #  Payment success
    path('success/', payment_success, name='payment_success'),

    # Optional features
    path('verify/', verify_payment, name='verify_payment'),
    path('track/', track_order, name='track_order'),
    path('invoice/', generate_invoice, name='invoice'),

    #  Order history
    path('history/', order_history, name='order_history'),
]