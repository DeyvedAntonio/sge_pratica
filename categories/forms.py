from django import forms
from .models import Category


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = [
            'name',
            'description',
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
            })
        }
