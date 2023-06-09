from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Personnel
from .forms import PersonnelForm

# Create your views here.
def personnel(request):
    """set up new page for displaying all content"""
    crew = Personnel.objects.filter(authorised=1)

    context = {
        'crew': crew,
    }

    return render(request, 'personnel/personnel.html', context)

def personnel_details(request, personnel_id):
    """create view to bring up the personnel specifics"""
    from_pending = False
    member = get_object_or_404(Personnel, pk=personnel_id)

    if member.authorised == 0:
        from_pending = True

    context = {
        'member': member,
        'from_pending': from_pending,
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
