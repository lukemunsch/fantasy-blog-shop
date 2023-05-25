from django.shortcuts import render, redirect, reverse, get_object_or_404

from .models import Personnel

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
