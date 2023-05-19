from django.shortcuts import render

from .models import News

# Create your views here.
def news(request):
    """set up your news updates view"""
    
    context = {
        
    }
    return render(request, 'news/news.html', context)