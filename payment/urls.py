from django.urls import path
from .views import homepage, paymenthandler

urlpatterns = [
    path("", homepage, name="razorpay_homepage"),
    path("paymenthandler", paymenthandler, name="razorpay_paymenthandler"),
]