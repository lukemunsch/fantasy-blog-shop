from django.shortcuts import render, reverse, redirect, get_object_or_404
from .models import Mission
# Create your views here.
def missions(request):
    """set up our standard missions page"""
    mission = Mission.objects.all()

    context = {
        'mission': mission,
    }

    return render(request, 'missions/missions.html', context)

def mission_details(request, mission_id):
    """Set up how we display our mission brief"""
    from_pending = False
    task = get_object_or_404(Mission, pk=mission_id)

    if task.approved_mission == 0:
        from_pending = True

    context = {
        'task': task,
        'from_pending': from_pending,
    }

    return render(request, 'missions/missions-details.html', context)
