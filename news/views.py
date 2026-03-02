from django.shortcuts import get_object_or_404, render

from .models import News


def news_list(request):
    items = News.objects.filter(is_published=True)
    return render(request, 'news/news_list.html', {'news_items': items})


def news_detail(request, slug):
    item = get_object_or_404(News, slug=slug, is_published=True)
    return render(request, 'news/news_detail.html', {'news': item})