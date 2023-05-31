from django.shortcuts import render, reverse, redirect, get_object_or_404

from .models import News

# Create your views here.
def news(request):
    """set up your news updates view"""
    news = News.objects.filter(approved_post=1)
    context = {
        'news': news,
    }
    return render(request, 'news/news.html', context)

def news_details(request, news_id):
    """set up our drill down into specific news entry"""
    from_pending = False

    event = get_object_or_404(News, pk=news_id)

    if event.approved_post == 0:
        from_pending = True

    context = {
        'event': event,
        'from_pending': from_pending,
    }

    return render(request, 'news/news-details.html', context)
