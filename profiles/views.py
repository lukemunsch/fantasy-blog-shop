from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserProfile

# Create your views here.
def profile(request):
    """set up our view for the profiles"""
    profile = get_object_or_404(UserProfile, user=request.user)

    context={
        'profile': profile,
    }

    return render(request, 'profiles/profile.html', )
