from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Personnel
from .forms import PersonnelForm, ApprovePersonnelForm

# Create your views here.


def personnel(request):
    """set up new page for displaying all content"""
    crew = Personnel.objects.filter(authorised=1)

    context = {
        'crew': crew,
    }

    return render(request, 'personnel/personnel.html', context)


@login_required
def pending_members(request):
    """set up our pending members authorisation page"""
    if not request.user.is_superuser:
        messages.error(
            request,
            'You are not authorised to access this Resource!'
        )
        return redirect(reverse('home'))

    crew = Personnel.objects.filter(authorised=0)

    context = {
        'crew': crew,
        'from_homepage': True,
    }

    return render(request, 'personnel/personnel.html', context)


def personnel_details(request, personnel_id):
    """create view to bring up the personnel specifics"""
    from_pending = False
    member = get_object_or_404(Personnel, pk=personnel_id)

    if member.authorised == 0:
        from_pending = True

    if request.method == 'POST':
        form = ApprovePersonnelForm(
            request.POST,
            instance=member
        )
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'You have successfully changed the approval of the member!'
            )
        else:
            messages.error(
                request,
                "You have failed to update this member's approval"
            )
    else:
        form = ApprovePersonnelForm(
            instance=member
        )

    context = {
        'member': member,
        'from_pending': from_pending,
        'form': form,
    }

    return render(request, 'personnel/personnel-details.html', context)


@login_required
def add_member(request):
    """ add new view for adding a member"""
    if not request.user.is_superuser:
        messages.error(
            request,
            'You are not authorised to access this Resource!'
        )
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = PersonnelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'A New Personnel is awaiting review!'
            )
            return redirect(reverse('pending_members'))
        else:
            messages.error(
                request,
                'Something went wrong - Please check through the form again!'
            )
    else:
        form = PersonnelForm()

    context = {
        'form': form,
    }
    return render(request, 'personnel/add-member.html', context)


@login_required
def edit_member(request, personnel_id):
    """set up our view for editing members"""
    if not request.user.is_superuser:
        messages.error(
            request,
            'You are not authorised to access this Resource!'
        )
        return redirect(reverse('personnel'))

    member = get_object_or_404(Personnel, pk=personnel_id)
    if request.method == 'POST':
        form = PersonnelForm(
            request.POST,
            request.FILES,
            instance=member
        )
        if form.is_valid():
            form.save()
            messages.success(
                request,
                f'Successfully updated { member.name }'
            )
            return redirect(reverse('personnel'))
        else:
            messages.error(
                request,
                'Failed to update Mission'
                'Please check through the form again!'
            )
    else:
        form = PersonnelForm(instance=member)
        messages.info(
            request,
            f'You are editing { member.name }'
        )

    context = {
        'member': member,
        'form': form,
    }
    return render(request, 'personnel/edit-member.html', context)
