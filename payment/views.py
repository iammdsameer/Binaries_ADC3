from django.shortcuts import render
from django.conf import settings
from django.contrib import messages
import stripe




stripe.api_key = settings.STRIPE_SECRET_KEY

# Create your views here.
def payment(request):
    publishKey = settings.STRIPE_PUBLISHABLE_KEY
    if request.method == "POST":
        token = request.POST['stripeToken']
        try:
            charge = stripe.Charge.create(
                amount=999, # Amount in dollars and cents
                currency='usd',
                description='Example charge',
                source=token
            )
            # User.objects.get(pk=pk).update(is_premium="True")
            messages.error(request, 'Payment Successfully Recieved.')
        except stripe.error.CardError as e:
            pass
    return render(request, 'payment/payment-update.html', {'publishKey': publishKey})