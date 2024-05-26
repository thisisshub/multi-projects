import razorpay
from django.conf import settings
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

razorpay_client = razorpay.Client(
    auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET)
)


def homepage(request):
    currency = settings.CURRENCY
    amount=request.GET["amount"]
    razorpay_order = razorpay_client.order.create(
        dict(
            amount=amount, currency=currency, payment_capture="1"
        )
    )
    callback_url = "paymenthandler/"
    context = {
        "razorpay_order_id": razorpay_order.get("id"),
        "razorpay_merchant_key": settings.RAZOR_KEY_ID,
        "razorpay_amount": amount,
        "currency": currency,
        "callback_url": callback_url,
    }

    return render(request, "payment.html", context=context)


@csrf_exempt
def paymenthandler(request):
    if request.method == "POST":
        try:
            payment_id = request.POST.get("razorpay_payment_id", "")
            razorpay_order_id = request.POST.get("razorpay_order_id", "")
            signature = request.POST.get("razorpay_signature", "")
            params_dict = {
                "razorpay_order_id": razorpay_order_id,
                "razorpay_payment_id": payment_id,
                "razorpay_signature": signature,
            }

            # verify the payment signature.
            result = razorpay_client.utility.verify_payment_signature(params_dict)
            if result is not None:
                amount = 20000 # Rs. 200
                try:
                    # capture the payemt
                    razorpay_client.payment.capture(payment_id, amount)
                    # render success page on successful caputre of payment
                    return render(request, "paymentsuccess.html")
                except:
                    # if there is an error while capturing payment.
                    return render(request, "paymentfail.html")
            else:
                # if signature verification fails.
                return render(request, "paymentfail.html")
        except Exception as e:
            return {"error": e}
    else:
        return {"error": "Your process could not be completed."}
