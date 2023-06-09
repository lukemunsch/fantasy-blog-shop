from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Personnel
from .forms import PersonnelForm

# Create your views here.
def personnel(request):
    """set up new page for displaying all content"""
    crew = Personnel.objects.all()

    context = {
        'crew': crew,
    }

    return render(request, 'personnel/personnel.html', context)

def personnel_details(request, personnel_id):
    """create view to bring up the personnel specifics"""
    member = get_object_or_404(Personnel, pk=personnel_id)

    context = {
        'member': member,
    }

    return render(request, 'personnel/personnel-details.html', context)

@login_required
def add_member(request):
    """ add new view for adding a member"""
    if not request.user.is_superuser:
        messages.error(
            request,
            'You are not authorised to Access this Resource!'
        )
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = PersonnelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                f'{{ personnel.name }} has been successfully added to the Roster'
            )
