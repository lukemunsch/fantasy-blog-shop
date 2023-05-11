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
