from django import forms
from .models import Inflow


class InflowForm(forms.ModelForm):

    class Meta:
        model = Inflow
        fields = [
            'suplier',
            'product',
            'description',
        ]
        exclude = [
            'quantity',
        ]
        widgets = {
            'suplier': forms.Select(attrs={'class': 'form-select'}),
            'product': forms.Select(attrs={'class': 'form-select'}),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 3,
                }
            ),
        }
