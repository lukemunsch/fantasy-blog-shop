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
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            messages.success(
                request,
                'New Article is awaiting your review!'
            )
            return redirect(reverse('pending_articles'))
        else:
            messages.error(
                request,
                'Something went wrong - Please check through the form again!'
            )
    else:
        form = NewsForm()

    context = {
        'form': form,
    }
    return render(request, 'news/add-news.html', context)

@login_required
def edit_news(request, news_id):
    """set up how we activate editing news articles"""
    if not request.user.is_superuser:
        messages.error(
            request,
            'You are not authorised to access this Resource!'
        )
        return redirect(reverse('missions'))

    news = get_object_or_404(News, pk=news_id)
    if request.method == 'POST':
        form = NewsForm(
            request.POST,
            request.FILES,
            instace=news
        )
        if form.is_valid():
            form.save()
            messages.success(
                request,
                f'Successfully updated { news.title }'
            )
            return redirect(reverse('news'))
        else:
            messages.error(
                request, (
                'Failed to update Mission'
                'Please check through the form again!'
                )
            )
    else:
        form = NewsForm(instance=news)
        messages.info(
            request,
            f'You are editing { news.title }'
        )

    context = {
        'news': news,
        'form': form,
    }
    return render(request, 'news/add-news.html', context)
