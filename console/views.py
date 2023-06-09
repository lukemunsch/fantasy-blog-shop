from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from personnel.models import Personnel
from news.models import News
from missions.models import Mission

# Create your views here.
def console(request):
    """set up new page for displaying all content"""
    crew = Personnel.objects.filter()[:5]
    news = News.objects.filter(approved_post=1)[:5]
    mission = Mission.objects.filter(approved_mission=1)[:5]

    context = {
        'crew': crew,
        'news': news,
        'mission': mission,
    }

    return render(request, 'console/console.html', context)

@login_required
def console_add_entry(request):
    """create view for our base add entry page"""
    if not request.user.is_superuser:
        messages.error(
            request,
            'Sorry, this page is for Grandmasters Only'
        )
        return redirect(reverse('home'))

    return render(request, 'console/console-add-entries.html')
