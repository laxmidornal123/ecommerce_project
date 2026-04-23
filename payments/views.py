from django.shortcuts import render

def payment_page(request):
    return render(request, 'payments/payment.html')