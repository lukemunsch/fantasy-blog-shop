from django.shortcuts import render

from personnel.models import Personnel
from news.models import News
from missions.models import Mission

# Create your views here.
def console(request):
    """set up new page for displaying all content"""
    crew = Personnel.objects.filter()[:5]
    news = News.objects.filter()[:5]
    mission = Mission.objects.filter()[:5]

    context = {
        'crew': crew,
        'news': news,
        'mission': mission,
    }

    return render(request, 'console/console.html', context)
