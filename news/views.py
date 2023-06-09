from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import News
from .forms import NewsForm

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


@login_required
def add_news(request):
    """set up our new view for adding a new article"""
    if not request.user.is_superuser:
        messages.error(
            request,
            'You are not authorised to access thie Resource!'
        )
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'This Article has been successfully posted to the pending news page!'
            )
            return redirect(reverse('home'))
    else:
        form = NewsForm()

    context = {
        'form': form,
    }
    return render(request, 'news/add-news.html', context)
