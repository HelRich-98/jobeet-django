from django.views.generic import CreateView, ListView, DetailView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.db.models import Count, Q
from django.core.paginator import Paginator

from .models import Job, Category
from .forms import JobForm


class JobListView(ListView):
    model = Job
    paginate_by = 10

    def get_queryset(self):
        queryset = Job.objects.filter(is_validate=True)

        q = self.request.GET.get("q")

        if q:
            queryset = queryset.filter(
                Q(title__icontains=q)
                | Q(description__icontains=q)
                | Q(company__name__icontains=q)
            )

        return queryset


class JobDetailView(DetailView):
    model = Job


class JobCreateView(CreateView):
    model = Job
    form_class = JobForm
    success_url = reverse_lazy("index")


class CategoryListView(ListView):
    model = Category
    paginate_by = 10
    queryset = Category.objects.annotate(job_count=Count("jobs"))


class CategoryDetailView(DetailView):
    model = Category

    def get_object(self, *args, **kwargs):
        name = self.kwargs.get("name", None)
        return get_object_or_404(Category, name=name)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        jobs_qs = self.object.jobs.select_related(
            "company",
            "category",
        ).order_by("-created_at")

        paginator = Paginator(jobs_qs, 10)
        page_number = self.request.GET.get("page")
        page = paginator.get_page(page_number)
        context["page_obj"] = page
        context["jobs"] = page

        return context
