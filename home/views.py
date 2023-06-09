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

@login_required
def pending_articles(request):
    """Set up our template for unapproved articles"""
    if not request.user.is_superuser:
        messages.error(
            request,
            'You are not authorised to access this Resource!'
        )
        return redirect(reverse('home'))

    news = News.objects.filter(approved_post=0)

    context = {
        'news': news,
        'from_homepage': True,
    }
    return render(request, 'news/news.html', context)


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
