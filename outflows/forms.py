from django import forms
from .models import Outflow


class OutflowForm(forms.ModelForm):

    class Meta:
        model = Outflow
        fields = [
            'product',
            'quantity',
            'description',
        ]
        widgets = {
            'product': forms.Select(attrs={
                'class': 'form-select',
            }),
            'quantity': forms.NumberInput(attrs={
                'class': 'form-control',
            }),
            'description': forms.TextArea(attrs={
                'class': 'form-control',
                'row': 3,
            }),
        }
    
    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        product = self.cleaned_data.get('product')

        if quantity > product.quantity:
            raise ValidationError(
                f'A quantidade disponível em estoque para o produto {product.title} é de {product.quantity}.'
            )
