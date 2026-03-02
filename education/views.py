from django.shortcuts import render

from departments.models import Department

from .models import Assessment, EducationDirection, EducationProcess, Practice


def directions(request):
    items = EducationDirection.objects.filter(is_active=True)
    return render(request, 'education/directions.html', {'directions': items})


def departments_list(request):
    items = Department.objects.all()
    return render(request, 'education/departments_list.html', {'departments': items})


def process(request):
    process_obj = EducationProcess.objects.first()
    return render(request, 'education/process.html', {'process': process_obj})


def assessment(request):
    assessment_obj = Assessment.objects.first()
    return render(request, 'education/assessment.html', {'assessment': assessment_obj})


def practice(request):
    practice_obj = Practice.objects.first()
    return render(request, 'education/practice.html', {'practice': practice_obj})