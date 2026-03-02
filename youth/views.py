from django.shortcuts import render

from .models import YouthActivity


def index(request):
    items = YouthActivity.objects.filter(is_active=True)
    return render(request, 'youth/index.html', {'activities': items})