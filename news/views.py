from django.db.models import F
from django.shortcuts import get_object_or_404, render

from .models import News


def news_list(request):
    items = News.objects.filter(is_published=True)
    return render(request, 'news/news_list.html', {'news_items': items})


def news_detail(request, slug):
    item = get_object_or_404(News, slug=slug, is_published=True)
    News.objects.filter(pk=item.pk).update(views_count=F('views_count') + 1)
    item.refresh_from_db(fields=['views_count'])
    return render(request, 'news/news_detail.html', {'news': item})
