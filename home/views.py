from django.shortcuts import render

# Create your views here.
def index(request):
    """set up your index view"""
    return render(request, 'home/index.html')
