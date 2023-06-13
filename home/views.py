from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required


from missions.models import Mission
from news.models import News
from personnel.models import Personnel

# Create your views here.
def index(request):
    """set up your index view"""
    missions = Mission.objects.filter(approved_mission=0)
    articles = News.objects.filter(approved_post=0)
    members = Personnel.objects.filter(authorised=0)

    context = {
        'missions': missions,
        'articles': articles,
        'members': members,
    }

    return render(request, 'home/index.html', context)
