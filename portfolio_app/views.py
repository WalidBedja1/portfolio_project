from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Project

def home(request):
    context = {
        'today': timezone.now().strftime('%d/%m/%Y')
    }
    return render(request, 'home.html', context)

def about(request):
    context = {
        'today': timezone.now().strftime('%d/%m/%Y')
    }
    return render(request, 'about.html', context)

def project_list(request):
    projects = Project.objects.all().order_by('-created_at')
    context = {
        'projects': projects,
        'count': projects.count(),
        'today': timezone.now().strftime('%d/%m/%Y')
    }
    return render(request, 'project_list.html', context)

def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    context = {
        'project': project,
        'today': timezone.now().strftime('%d/%m/%Y')
    }
    return render(request, 'project_detail.html', context)

def recent_projects(request):
    projects = Project.objects.all().order_by('-created_at')[:3]
    context = {
        'projects': projects,
        'count': projects.count(),
        'today': timezone.now().strftime('%d/%m/%Y')
    }
    return render(request, 'recent_projects.html', context)