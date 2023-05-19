from django.shortcuts import render

# Create your views here.

def news(request):
    """set up our view for news updates"""
    return render(request, 'news/news.html, context')