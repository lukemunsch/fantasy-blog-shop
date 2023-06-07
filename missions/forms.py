from django import forms

from .models import Mission
from .widgets import CustomClearableFileInput

class MissionForm(forms.ModelForm):
    """
    Form for creating a new mission to go 
    into our pending list
    """
    class Meta:
        model = Mission
        fields = [
            'mission',
            'mission_grade',
            'mission_lead',
            'prep_time',
            'mission_length',
            'mission_status',
            'mission_img',
            'img_url',
        ]
