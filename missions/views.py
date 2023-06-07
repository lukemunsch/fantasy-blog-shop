from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Mission
from .forms import MissionForm

# Create your views here.
def missions(request):
    """set up our standard missions page"""
    mission = Mission.objects.filter(approved_mission=1)

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

@login_required
def add_mission(request):
    """set up our new view for adding a new mission"""
    if not request.user.is_superuser:
        message.error(
            request,
            'Sorry, You cannot access this function!'
        )
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = MissionForm(request.POST)
        if form.is_valid():
            form.save()
            message.success(
                request,
                'New Mission is waiting your approval!'
            )
            return redirect(reverse('home'))
        else:
            messages.error(
                request,
                'Failed to create Mission - Ensure all details are correct!'
            )
    else:
        form = MissionForm()

    context = {
        'form': form,
    }
    return render(request, 'mission/add-mission.html', context)
