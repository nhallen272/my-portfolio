from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("index/", views.index, name='index'),
    path("about/", views.about, name='about'),
    path("contact/", views.contact, name='contact'),
    path("projects/", views.project_index, name="project_index"),
    path("projects/<int:pk>/", views.project_detail, name="project_detail"),
    path("projects/<str:cat>/", views.project_category, name="project_category")
]