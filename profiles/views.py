from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm

# Create your views here.
def profile_page(request):
    """Set up our view to implement a view of our profiles"""
    profile = get_object_or_404(UserProfile, user=request.user)
    context = {
    }
    return render(request, 'profiles/profile.html', context)
