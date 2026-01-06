from django.views.generic import CreateView, ListView, DetailView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

from .models import Job, Category
from .forms import JobForm


class JobListView(ListView):
    model = Job
    paginate_by = 10


class JobDetailView(DetailView):
    model = Job


class JobCreateView(CreateView):
    model = Job
    form_class = JobForm
    success_url = reverse_lazy("index")


class CategoryListView(ListView):
    model = Category
    paginate_by = 10


class CategoryDetailView(DetailView):
    model = Category

    def get_object(self, *args, **kwargs):
        name = self.kwargs.get("name", None)
        return get_object_or_404(Category, name=name)
