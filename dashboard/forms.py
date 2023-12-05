from django import forms
from app.models import Website

class WebsiteForm(forms.ModelForm):
    class Meta:
        model = Website
        fields = ('name', 'url', 'description', 'category')