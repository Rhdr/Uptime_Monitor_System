from django import forms
from django.db.models import fields
from .models import Website


class WebsiteAddUpdateForm(forms.ModelForm):
    # site_name = forms.CharField()
    # site_url = forms.URLField()
    # slack_account_url = forms.URLField()

    class Meta:
        model = Website
        fields = ("site_name", "site_url", "slack_token", "slack_channel")