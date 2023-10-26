from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserProfile
from checkout.models import Order
from .forms import UserProfileForm


def profile(request):
    """display the user's profle"""
    profile = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile Successfully Updated')
        else:
            messages.error(request, (
                'Update failed. Please ensure '
                'the form is valid.'))
    else:
        form = UserProfileForm(instance=profile)

    orders = profile.orders.all()

    context = {
        'profile': profile,
        'form': form,
        'orders': orders,
        'on_profile_page': True,
    }

    return render(request, 'user_profiles/profiles.html', context)

def order_history(request, order_number):
    """set up new view for order history"""
    order = get_object_or_404(Order, order_number=order_number)
    messages.info(request, f'This is a previous confirmation for the order number {order_number}. \
                  You should have received and email on the order date.')
    
    context = {
        'order': order,
        'from_profile': True,
    }
    return render(request, 'checkout/checkout_success.html', context)
