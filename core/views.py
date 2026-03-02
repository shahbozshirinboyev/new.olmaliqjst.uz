from django.shortcuts import render

from news.models import News

from .models import About, Document, Leadership, MaterialBase


def home(request):
    latest_news = News.objects.filter(is_published=True)[:3]
    leaders = Leadership.objects.all()[:3]
    context = {
        'latest_news': latest_news,
        'leaders': leaders,
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