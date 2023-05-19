from django.shortcuts import render

# Create your views here.
def news(request):
    """set up your news updates view"""
    return render(request, 'news/news.html')