from django.shortcuts import render

# Create your views here.
def profile(request):
    """set up our view for the profiles"""
    context={}

    return render(request, 'profiles/profile.html', )
