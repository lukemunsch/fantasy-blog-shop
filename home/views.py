from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required


from missions.models import Mission, Update
from news.models import News
from personnel.models import Personnel

# Create your views here.
def index(request):
    """set up your index view"""
    missions = Mission.objects.filter(approved_mission=0)
    articles = News.objects.filter(approved_post=0)
    members = Personnel.objects.filter(authorised=0)
    updates = Update.objects.filter(approved=0)

    context = {
        'missions': missions,
        'articles': articles,
        'members': members,
        'updates': updates,
    }

    return render(request, 'home/index.html', context)
