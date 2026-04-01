from django.db.models import F
from django.shortcuts import get_object_or_404, render

from education.models import EducationDirection
from news.models import News

from .models import About, Announcement, Document, Leadership, MaterialBase, TechStat


def home(request):
    latest_news = News.objects.filter(is_published=True)[:3]
    directions = EducationDirection.objects.filter(is_active=True)
    tech_stats = TechStat.objects.filter(is_active=True)
    announcements = Announcement.objects.filter(is_active=True).order_by('-published_at', '-created_at')[:6]
    context = {
        'latest_news': latest_news,
        'directions': directions,
        'tech_stats': tech_stats,
        'announcements': announcements,
    }
    return render(request, 'core/home.html', context)


def about(request):
    about_obj = About.objects.first()
    return render(request, 'core/about.html', {'about': about_obj})


def leadership(request):
    leaders = Leadership.objects.all()
    return render(request, 'core/leadership.html', {'leaders': leaders})


def material_base(request):
    materials = MaterialBase.objects.all()
    return render(request, 'core/material_base.html', {'materials': materials})


def documents(request):
    docs = Document.objects.all()
    return render(request, 'core/documents.html', {'documents': docs})


def announcements_list(request):
    announcements = Announcement.objects.filter(is_active=True).order_by('-published_at', '-created_at')
    return render(request, 'core/announcement_list.html', {'announcements': announcements})


def announcement_detail(request, pk):
    announcement = get_object_or_404(Announcement, pk=pk, is_active=True)
    Announcement.objects.filter(pk=announcement.pk).update(views_count=F('views_count') + 1)
    announcement.refresh_from_db(fields=['views_count'])
    return render(request, 'core/announcement_detail.html', {'announcement': announcement})
