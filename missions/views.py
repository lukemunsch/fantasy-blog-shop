from django.shortcuts import render
from .models import Mission
# Create your views here.
def missions(request):
    """set up our standard missions page"""
    mission = Mission.objects.all()

    context = {
        'mission': mission,
    }

    return render(request, 'missions/missions.html', context)
