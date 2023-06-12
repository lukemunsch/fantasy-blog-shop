from django import forms
from django.forms import Select

from .models import Mission
from personnel.models import Personnel
from .widgets import CustomClearableFileInput



class MissionForm(forms.ModelForm):
    """
    Form for creating a new mission to go 
    into our pending list
    """
    def __init__(self, *args, **kwargs):
        super(MissionForm, self).__init__(*args, **kwargs)
        self.fields['prep_time'].label = 'Preparation Time (in days)'
        self.fields['mission_length'].label = 'Mission Length (in weeks)'

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
            'approved_mission',
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
                attrs={
                    'placeholder': 'Add Mission Description Here'
                }
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
            'approved_mission': forms.Select(
                attrs={
                    'style': 'width: 200px;',
                }
            )
        }

    mission_img = forms.ImageField(
        label='Image Upload',
        required=False,
        widget=CustomClearableFileInput,
    )
