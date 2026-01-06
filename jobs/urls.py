from django.urls import path

from . import views

app_name = "jobs"

urlpatterns = [
    path(
        "list/",
        views.JobListView.as_view(),
        name="job_list",
    ),
    path(
        "detail/<slug>/",
        views.JobDetailView.as_view(),
        name="job_detail",
    ),
    path(
        "create/",
        views.JobCreateView.as_view(),
        name="job_create",
    ),
    path(
        "categories/",
        views.CategoryListView.as_view(),
        name="category_list",
    ),
    path(
        "category/<name>/",
        views.CategoryDetailView.as_view(),
        name="category_detail",
    ),
]
