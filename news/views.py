from django.shortcuts import render, reverse, redirect, get_object_or_404

from .models import News

# Create your views here.
def news(request):
    """set up your news updates view"""
    news = News.objects.all()
    context = {
        'news': news,
    }
    return render(request, 'news/news.html', context)

def news_details(request, news_id):
    """set up our drill down into specific news entry"""
    event = get_object_or_404(News, pk=news_id)

    context = {
        'event': event,
    }

    return render(request, 'news/news-details.html', context)
