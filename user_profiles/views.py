from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserProfile
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
        form = UserProfileForm()

    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'user_profiles/profiles.html', context)
