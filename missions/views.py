from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Mission, Update
from .forms import (
    MissionForm,
    ApproveMissionForm,
    UpdateForm,
    ApproveUpdateForm
)

# Create your views here.


def missions(request):
    """set up our standard missions page"""
    mission = Mission.objects.filter(approved_mission=1)

    context = {
        'mission': mission,
        'from_mission': True,
    }

    return render(request, 'missions/missions.html', context)


@login_required
def pending_missions(request):
    """set up our template for unapproved missions"""
    if not request.user.is_superuser:
        messages.error(
            request,
            'You are not authorised to access this Resource!'
        )
        return redirect(reverse('home'))

    mission = Mission.objects.filter(approved_mission=0)

    context = {
        'mission': mission,
        'from_homepage': True,
    }
    return render(request, 'missions/missions.html', context)


def mission_details(request, mission_id):
    """Set up how we display our mission brief"""
    from_pending = False
    mission = get_object_or_404(Mission, pk=mission_id)
    update = Update.objects.filter(approved=1)

    if mission.approved_mission == 0:
        from_pending = True

    if request.method == 'POST':
        form = ApproveMissionForm(
            request.POST,
            instance=mission
        )
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'You have successfully changed the approval of the mission!'
            )
            if mission.approved_mission == 0:
                from_pending = True
            else:
                from_pending = False
        else:
            messages.error(
                request,
                "You have failed to update this mission's approval"
            )
    else:
        form = ApproveMissionForm(instance=mission)

    context = {
        'mission': mission,
        'from_pending': from_pending,
        'form': form,
        'update': update,
    }

    return render(request, 'missions/mission-details.html', context)


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


@login_required
def edit_mission(request, mission_id):
    """Set up our page for editing missions"""
    if not request.user.is_superuser:
        messages.error(
            request,
            'You are not authorised to access this Resource!'
        )
        return redirect(reverse('home'))

    mission = get_object_or_404(Mission, pk=mission_id)
    if request.method == 'POST':
        form = MissionForm(
            request.POST,
            request.FILES,
            instance=mission
        )

        if form.is_valid():
            form.save()
            messages.success(
                request,
                f'Successfully update { mission.mission }!'
            )
            return redirect(reverse('missions'))
        else:
            messages.error(request, (
                'Failed to update Mission'
                'Please check through the form again!'
            ))
    else:
        form = MissionForm(instance=mission)
        messages.info(
            request,
            f'You are editing { mission.mission }'
        )

    context = {
        'mission': mission,
        'form': form,
    }
    return render(request, 'missions/edit-mission.html', context)


@login_required
def delete_mission(request, mission_id):
    """set up our view to delete missions"""
    if not request.user.is_superuser:
        messages.error(
            request,
            'You are not authorised to access this Resource!'
        )
        return redirect(reverse('home'))

    mission = get_object_or_404(Mission, pk=mission_id)
    if request.method == 'POST':
        mission.delete()
        messages.success(
            request,
            f'You have successfully deleted { mission.mission }'
        )
        return redirect(reverse('missions'))

    context = {
        'mission': mission,
    }
    return render(request, 'missions/delete-mission.html', context)


@login_required
def add_update(request, mission_id):
    """set up a view for adding an update"""
    if not request.user.is_superuser:
        messages.error(
            request,
            'You are not authorised to access this Resource!'
        )
        return redirect(reverse('home'))

    mission = get_object_or_404(Mission, pk=mission_id)
    if request.method == 'POST':
        form = UpdateForm(
            request.POST
        )
        if form.is_valid():
            form.instance.mission = mission
            form.save()
            messages.success(
                request,
                f'You have added an Update to { mission.mission }'
            )
            return redirect(reverse('missions'))
    else:
        form = UpdateForm()

    context = {
        'mission': mission,
        'form': form,
    }

    return render(request, 'missions/add_update.html', context)


@login_required
def pending_updates(request):
    """set up a view for all the updates"""
    if not request.user.is_superuser:
        messages.error(
            request,
            'You are not authorised to access this Resource!'
        )
        return redirect(reverse('home'))

    updates = Update.objects.filter(approved=0)

    context = {
        'updates': updates,
    }

    return render(request, 'missions/pending-updates.html', context)

@login_required
def update_details(request, update_id):
    """set up the view to fully display an update"""
    if not request.user.is_superuser:
        messages.error(
            request,
            'You are not authorised to access this Resource!'
        )
        return redirect(reverse('home'))

    update = get_object_or_404(Update, pk=update_id)

    if request.method == 'POST':
        form = ApproveUpdateForm(
            request.POST,
            instance=update
        )
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'You have successfully changed the approval of the update!'
            )
        else:
            messages.error(
                request,
                "You have failed to approve this Update!"
            )
    else:
        form = ApproveUpdateForm(instance=update)

    context = {
        'update': update,
        'form': form,
    }

    return render(request, 'missions/update-details.html', context)

@login_required
def edit_update(request, update_id):
    """Set up our page for editing missions"""
    if not request.user.is_superuser:
        messages.error(
            request,
            'You are not authorised to access this Resource!'
        )
        return redirect(reverse('home'))

    update = get_object_or_404(Update, pk=update_id)

    if request.method == 'POST':
        form = UpdateForm(
            request.POST,
            instance=update
        )

        if form.is_valid():
            form.save()
            messages.success(
                request,
                f'Successfully update { update.title }!'
            )
            return redirect('update_details', update_id)
        else:
            messages.error(request, (
                'Failed to edit Update'
                'Please check through the form again!'
            ))
    else:
        form = UpdateForm(instance=update)
        messages.info(
            request,
            f'You are editing { update.title }'
        )

    context = {
        'update': update,
        'form': form,
    }
    return render(request, 'missions/edit-update.html', context)

@login_required
def delete_update(request, update_id):
    """set up our view to delete missions"""
    if not request.user.is_superuser:
        messages.error(
            request,
            'You are not authorised to access this Resource!'
        )
        return redirect(reverse('home'))

    update = get_object_or_404(Update, pk=update_id)
    if request.method == 'POST':
        update.delete()
        messages.success(
            request,
            f'You have successfully deleted { update.title }'
        )
        return redirect(reverse('missions'))

    context = {
        'update': update,
    }
    return render(request, 'missions/delete-update.html', context)
