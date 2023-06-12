from django import forms
from django.forms import Select

from .models import Personnel
from missions.widgets import CustomClearableFileInput


class PersonnelForm(forms.ModelForm):
    """set up our personnel form to add new members"""
    class Meta:

        model = Personnel
        fields = [
            'name',
            'age',
            'originated_from',
            'rank',
            'speciality',
            'current_status',
            'profile_image',
            'image_url',
            'authorised',
        ]
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Full Name Here',
                }
            ),
            'age': forms.NumberInput(
                attrs={
                    'style': 'width: 100px;',
                }
            ),
            'originated_from': forms.TextInput(
                attrs={
                    'placeholder': 'Please Enter Hometown Area'
                }
            ),
            'rank': forms.Select(
                attrs={
                    'style': 'width: 200px;',
                }
            ),
            'speciality': forms.Textarea(
                attrs={
                    'placeholder': 'Enter Charcter Info Here',
                }
            ),
            'current_status': forms.Select(
                attrs={
                    'style': 'width: 200px;',
                }
            ),
            'image_url': forms.TextInput(
                attrs={
                    'placeholder': 'Online Image URL'
                }
            ),
            'authorised': forms.Select(
                attrs={
                    'style': 'width: 200px;',
                }
            )
        }

    profile_image = forms.ImageField(
        label='Image Upload',
        required=False,
        widget=CustomClearableFileInput,
    )
