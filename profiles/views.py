from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm

# Create your views here.
def profile_page(request):
    """Set up our view to implement a view of our profiles"""
    profile = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'You have updated your profile details'
            )
        else:
            messages.error(
                request,
                'You have failed to update your details'
            )
    else:
        form = UserProfileForm()
    context = {
        'form': form,
    }
    return render(request, 'profiles/profile.html', context)
