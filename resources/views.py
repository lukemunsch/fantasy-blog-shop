from django.shortcuts import render

# Create your views here.
def resources(request):
    """set up shop for our resources"""
    return render(request, 'resources/resources.html')
