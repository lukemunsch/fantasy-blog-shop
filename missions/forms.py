from django import forms
from django.forms import Select

from .models import Mission
from personnel.models import Personnel
from .widgets import CustomClearableFileInput

GRADES = (
    (1, 'Extreme'),
    (2, 'Dangerous'),
    (3, 'Serious'),
    (4, 'Moderate'),
    (5, 'Basic'),
    (6, 'Training')
)
STATUS = (
    (1, 'Active'),
    (2, 'Completed'),
    (3, 'On Hold'),
    (4, 'Cancelled')
)
PUBLISH = ((0, 'Hidden'), (1, 'Displayed'))

class MissionForm(forms.ModelForm):
    """
    Form for creating a new mission to go 
    into our pending list
    """
    class Meta:
        """set up our form widgets"""
        model = Mission
        fields = [
            'mission',
            'mission_grade',
            'mission_lead',
            'prep_time',
            'mission_length',
            'mission_img',
            'img_url',
            'description',
        ]
        widgets = {
            'mission': forms.TextInput(
                attrs={
                    'placeholder': 'Mission Title Here',
                }
            ),
            'mission_lead': Select(
                attrs={
                    'style': 'width: 200px;',
                }
            ),
            'mission_grade': forms.RadioSelect(),
            'img_url': forms.TextInput(
                attrs={'placeholder': 'Online Image URL'}
            ),
            'description': forms.Textarea(
                attrs={'placeholder': 'Add Mission Description Here'}
            ),
            'prep_time': forms.NumberInput(
                attrs={
                    'style': 'width: 100px;',
                }
            ),
            'mission_length': forms.NumberInput(
                attrs={
                    'style': 'width: 100px;',
                }
            ),
        }

    mission_img = forms.ImageField(
        label='Image Upload',
        required=False,
        widget=CustomClearableFileInput,
    )
