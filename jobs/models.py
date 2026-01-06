from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

# JOB CATEGORY


class Category(models.Model):
    name = models.CharField(_("Nom"), max_length=50, unique=True)
    description = models.TextField(_("Description"), blank=True)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("jobs:category_detail", kwargs={"name": self.name})


# COMPANY


class Company(models.Model):
    name = models.CharField(_("Nom"), max_length=80)
    logo = models.ImageField(_("Logo"), upload_to="companies/logos/")
    website = models.URLField(
        _("Site web"),
        max_length=200,
        null=True,
        blank=True,
    )
    location = models.CharField(_("Localisation"), max_length=100)
    email = models.EmailField(_("Email"), max_length=254)

    class Meta:
        verbose_name = _("Company")
        verbose_name_plural = _("Companies")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("jobs:company_detail", kwargs={"pk": self.pk})


# JOB


class Job(models.Model):
    JOB_TYPES = [
        ("full_time", "Temps plein"),
        ("part_time", "Temps partiel"),
        ("contract", "Contrat"),
        ("internship", "Stage"),
        ("temporary", "Temporaire"),
    ]

    title = models.CharField(_("Titre"), max_length=250, unique=True)
    slug = models.SlugField(_("Slug"))
    position = models.CharField(_("Position"), max_length=250)
    description = models.TextField(_("Description"))

    location = models.CharField(_("Localisation"), max_length=100)
    job_type = models.CharField(
        max_length=20,
        choices=JOB_TYPES,
        default="Temps plein",
    )
    is_validate = models.BooleanField(_("Est valide"), default=False)
    category = models.ForeignKey(
        "Category",
        verbose_name=_("Catégorie"),
        on_delete=models.CASCADE,
        related_name="jobs",
    )
    company = models.ForeignKey(
        "Company",
        verbose_name=_("Entreprise"),
        on_delete=models.CASCADE,
        related_name="jobs",
    )

    created_at = models.DateField(
        _("Date de publication"),
        auto_now_add=True,
    )
    updated_at = models.DateField(
        _("Date de mise a jour"),
        auto_now=True,
    )
    expired_at = models.DateField(
        _("Date d'expiration"),
    )

    class Meta:
        verbose_name = _("Job")
        verbose_name_plural = _("Jobs")
        ordering = ("-created_at", "title")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("jobs:job_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)
