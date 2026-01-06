from django import forms

from .models import Job


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = (
            "category",
            "company",
            "title",
            "position",
            "location",
            "job_type",
            "description",
            "expired_at",
            "is_valid",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["category"].widget.attrs.update({"class": "select"})
        self.fields["company"].widget.attrs.update({"class": "select"})
        self.fields["title"].widget.attrs.update({"class": "input"})
        self.fields["position"].widget.attrs.update({"class": "input"})
        self.fields["location"].widget.attrs.update({"class": "input"})
        self.fields["description"].widget.attrs.update({"class": "textarea"})
        self.fields["expired_at"].widget.attrs.update(
            {"class": "input max-w-sm", "placeholder": "DD-MM-YYYY"}
        )
