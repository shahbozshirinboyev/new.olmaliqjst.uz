from django.shortcuts import get_object_or_404, render

from .models import Department, DepartmentHead


def department_list(request):
    items = Department.objects.all()
    return render(request, 'departments/department_list.html', {'departments': items})


def department_detail(request, slug):
    item = get_object_or_404(Department, slug=slug)
    teachers = item.teacher_set.all()
    return render(
        request,
        'departments/department_detail.html',
        {'department': item, 'teachers': teachers},
    )


def department_head_detail(request, pk):
    head = get_object_or_404(DepartmentHead, pk=pk)
    return render(request, 'departments/department_head_detail.html', {'head': head})
