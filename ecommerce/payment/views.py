from django.shortcuts import render
from .models import ShippingAddress

def checkout(request):
    if request.user.is_authenticated:
        try:
            shipping = ShippingAddress.objects.get(user=request.user.id)
            context = {'shipping': shipping}

            return render(request, 'payment/checkout.html', context)
        except:
            return render(request, 'payment/checkout.html')


    return render(request, 'payment/checkout.html')

def payment_success(request):
    return render(request, 'payment/payment-success.html')

def payment_failed(request):
    return render(request, 'payment/payment-failed.html')