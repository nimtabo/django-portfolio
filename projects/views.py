from django.shortcuts import render

from projects.models import Project

# Create your views here.
def ProjectList(request):
    projects = Project.objects.all()
    context = {"projects": projects}
    return render(request, "project_list.html", context)


# class ProjectList(request):
#     projects = Project.objects.all()
#     context = {"projects": projects}
#     return render(request, "project_list.html", context)


# class ProjectDetails(request, pk):
#     project = Project.objects.get(pk=pk)
#     context = {"project": project}
#     return render(request, "project_details.html", context)


def ProjectDetails(request, pk):
    project = Project.objects.get(pk=pk)
    context = {"project": project}
    return render(request, "project_details.html", context)
