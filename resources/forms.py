from django import forms
from django.forms import Select

from missions.widgets import CustomClearableFileInput

from .models import Product

class ProductForm(forms.ModelForm):
    """st up our new additional product form"""
    class Meta:
        """set up how our form works"""
        model = Product
        fields = [
            'name',
            'description',
            'price',
            'category',
            'approved_item',
            'image',
        ]
        widgets = {
            'name': forms.TextInput(
                attrs={'placeholder': 'Give the product a name (size)'}
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Enter Product description here',
                }
            ),
            'price': forms.NumberInput(
                attrs={
                    'style': 'width: 200px;',
                    'placeholder': 'Enter Price',
                }
            ),
            'category': forms.Select(
                attrs={
                    'style': 'width: 200px;',
                }
            ),
            'approved_item': forms.Select(
                attrs={
                    'style': 'width: 200px;',
                }
            )
        }

    image = forms.ImageField(
        label='Image',
        required=False,
        widget=CustomClearableFileInput
    )

class ApproveProductForm(forms.ModelForm):
    """set up a new form for approving items"""
    def __init__(self, *args, **kwargs):
        super(ApproveProductForm, self).__init__(*args, **kwargs)
        self.fields['approved_item'].label = 'How would you like to display this item?'
    class Meta:
        """specific form details"""
        model = Product
        fields = [
            'approved_item'
        ]
        widgets = {
            'approved_item': forms.Select(
                attrs={
                    'style': 'width: 100%',
                }
            )
        }
