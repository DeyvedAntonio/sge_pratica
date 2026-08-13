from django import forms
from django.forms import ModelForm
from .models import Brand


class BrandForm(ModelForm):

    class Meta:
        model = Brand
        fields = [
            'name',
            'description',
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3})
        }
        labels = {
            'name': 'nome',
            'description': 'descrição',
        }
