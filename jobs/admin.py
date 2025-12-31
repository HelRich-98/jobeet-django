from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import Category, Company, Job


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ("name", "jobs_count")

    @admin.display(description="Jobs")
    def jobs_count(self, category):
        return category.jobs.count()


@admin.register(Company)
class CompanyAdmin(ModelAdmin):
    list_display = (
        "name",
        "email",
        "website",
        "location",
        "jobs_count",
    )

    @admin.display(description="Jobs")
    def jobs_count(self, company):
        return company.jobs.count()


@admin.register(Job)
class JobAdmin(ModelAdmin):
    list_display = (
        "position",
        "title",
        "category",
        "company",
        "expired_at",
        "is_validate",
    )
    prepopulated_fields = {
        "slug": ("title",),
    }
