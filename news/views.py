from django.shortcuts import render

from .models import News

# Create your views here.
def news(request):
    """set up your news updates view"""
    news = News.objects.all()
    context = {
        'news': news,
    }
    return render(request, 'news/news.html', context)