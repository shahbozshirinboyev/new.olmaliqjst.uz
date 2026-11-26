from django.shortcuts import render

from departments.models import Department

from .models import Assessment, Control, EducationDirection, EducationProcess, Graduate, Practice


def directions(request):
    items = EducationDirection.objects.filter(is_active=True)
    return render(request, 'education/directions.html', {'directions': items})


def departments_list(request):
    items = Department.objects.all()
    return render(request, 'education/departments_list.html', {'departments': items})


def process(request):
    process_list = EducationProcess.objects.order_by('-created_at')
    return render(request, 'education/process.html', {'processes': process_list})


def assessment(request):
    assessment_obj = Assessment.objects.all()
    control_obj = Control.objects.all()
    return render(
        request,
        'education/assessment.html',
        {
            'assessment': assessment_obj,
            'control': control_obj,
        },
    )


def practice(request):
    practices = Practice.objects.filter(is_active=True)
    graduates = Graduate.objects.filter(is_active=True)
    return render(request, 'education/practice.html', {'practices': practices, 'graduates': graduates})
