from fake import (
    FACTORY,
    DjangoModelFactory,
    pre_init,
    FileSystemStorage,
)
from django.utils.text import slugify
from django.conf import settings

from .models import Category, Company, Job

STORAGE = FileSystemStorage(root_path=settings.MEDIA_ROOT, rel_path="tmp")


class CompanyFactory(DjangoModelFactory):
    name = FACTORY.name()
    email = FACTORY.company_email()
    website = FACTORY.domain_name()
    logo = FACTORY.png_file(storage=STORAGE, size=(250, 250))
    location = FACTORY.city()

    class Meta:
        model = Company


class JobFactory(DjangoModelFactory):
    title = FACTORY.sentence()
    description = FACTORY.text()
    position = FACTORY.sentence()
    location = FACTORY.city()
    is_validate = FACTORY.pybool()
    expired_at = FACTORY.date(start_date="0d", end_date="+30d")

    class Meta:
        model = Job

    @pre_init
    def on_pre_init(self, data):
        from random import choice

        cat = choice(Category.objects.all())
        comp = choice(Company.objects.all())

        data["category"] = cat
        data["company"] = comp
        data["slug"] = slugify(data["title"])
