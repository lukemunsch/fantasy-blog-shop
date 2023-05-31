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
    """Set up our GET request for unapproved articles"""
    ua_articles = News.objects.filter(approved_post=0)

    context = {
        'ua_articles': ua_articles,
    }
    render(request, 'news/news.html', context)
