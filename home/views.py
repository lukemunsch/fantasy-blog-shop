from django.shortcuts import render
from missions.models import Mission
from news.models import News

# Create your views here.
def index(request):
    """set up your index view"""
    missions = Mission.objects.filter(approved_mission=0)
    articles = News.objects.filter(approved_post=0)

    context = {
        'missions': missions,
        'articles': articles,
    }

    return render(request, 'home/index.html', context)

def pending_articles(request):
    """Set up our template for unapproved articles"""
    news = News.objects.filter(approved_post=0)

    context = {
        'news': news,
        'from_homepage': True
    }
    return render(request, 'news/news.html', context)

def pending_missions(request):
    """set up our tempalte for unapproved missions"""
    mission = Mission.objects.filter(approved_mission=0)

    context = {
        'mission': mission,
        'from_homepage': True
    }
    return render(request, 'missions/missions.html', context)
