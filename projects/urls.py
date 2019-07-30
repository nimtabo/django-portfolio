from django.urls import path
from . import views

urlpatterns = [
  path('', views.ProjectList, name="project_list"),
  path('<int:pk>/', views.ProjectDetails, name='project_details'),
]