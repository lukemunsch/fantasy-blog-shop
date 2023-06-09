from django import forms

from .models import Personnel
from missions.widgets import CustomClearableFileInput

class PersonnelForm(forms.ModelForm):
    """set up our personnel form to add new members"""
    model = Personnel
    