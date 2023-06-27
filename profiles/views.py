from django.shortcuts import render

# Create your views here.
def profile(request):
    """Set up our view to implement a view of our profiles"""
    return render(request, 'profiles/profile.html')
