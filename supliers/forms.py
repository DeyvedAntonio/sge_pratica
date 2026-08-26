from django import forms
from .models import Suplier


class SuplierForm(forms.ModelForm):

    class Meta:
        model = Suplier
        fields = [
            'name',
            'description',
        ]
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'row': 3,
            }),
        }