from django.shortcuts import render

from education.models import EducationDirection
from news.models import News

from .models import About, Announcement, Document, Leadership, MaterialBase, TechStat


def home(request):
    latest_news = News.objects.filter(is_published=True)[:3]
    directions = EducationDirection.objects.filter(is_active=True)
    tech_stats = TechStat.objects.filter(is_active=True)
    announcements = Announcement.objects.filter(is_active=True).order_by('-published_at', '-created_at')[:4]
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
    material = MaterialBase.objects.first()
    return render(request, 'core/material_base.html', {'material': material})


def documents(request):
    docs = Document.objects.all()
    return render(request, 'core/documents.html', {'documents': docs})
