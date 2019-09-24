from django.urls import reverse
from django.shortcuts import render , get_object_or_404
from decimal import Decimal
from paypal.standard.forms import PayPalPaymentsForm
from orders.models import Order
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def payment_done(request):
    return render(request,'homepage/done.html')

@csrf_exempt
def payment_canceled(request):
    return render(request,'homepage/canceled.html')

def payment_process(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order,id = order_id)
    host = request.get_host()

    # What you want the button to do.
    paypal_dict = {
        'business': "setting.PAYPAL_RECEIVER_EMAIL",
        "amount": '%.2f' % Decimal(order.get_total_cost()).quantize(Decimal('.01')),
        "item_name": "Order {}".format(order.id),
        "invoice": str(order.id),
        "currency_code": 'USD',
        "notify_url": 'http://{}{}'.format(host,reverse('paypal-ipn')),
        "return_url": 'http://{}{}'.format(host,reverse('payment:done')),
        "cancel_return": 'http://{}{}'.format(host,reverse('payment:canceled')),
        #"custom": "premium_plan",  # Custom command to correlate to some function later (optional)
    }

    # Create the instance.
    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request, "homepage/process.html", {'order':order,
                                                    'form':form})
