from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib import messages
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
        messages.error(
            request,
            'You are not authorised to access this Resource!'
        )
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = MissionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'New Mission is awaiting review!'
            )
            return redirect(reverse('pending_missions'))
        else:
            messages.error(
                request,
                'Something went wrong - Please check through the form again!'
            )
    else:
        form = MissionForm()

    context = {
        'form': form,
    }
    return render(request, 'missions/add-mission.html', context)
