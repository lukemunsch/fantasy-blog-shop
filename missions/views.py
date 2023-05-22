from django.shortcuts import render

# Create your views here.
def missions(request):
    """set up our standard missions page"""
    return render(request, 'missions/missions.html')