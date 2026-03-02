from django.shortcuts import get_object_or_404, render

from .models import Teacher


def teacher_list(request):
    items = Teacher.objects.select_related('department').all()
    return render(request, 'faculty/teacher_list.html', {'teachers': items})


def teacher_detail(request, pk):
    item = get_object_or_404(Teacher.objects.select_related('department'), pk=pk)
    return render(request, 'faculty/teacher_detail.html', {'teacher': item})