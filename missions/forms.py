from django import forms
from django.forms import Select

from personnel.models import Personnel
from .models import Mission, Update

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
        self.fields['approved_mission'].label = 'Approve Mission?'

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

    mission_lead = forms.ModelChoiceField(
        queryset=Personnel.objects.filter(authorised=1)
    )
    mission_img = forms.ImageField(
        label='Image Upload',
        required=False,
        widget=CustomClearableFileInput,
    )


class ApproveMissionForm(forms.ModelForm):
    """Set up form for pending mission approval"""
    def __init__(self, *args, **kwargs):
        super(ApproveMissionForm, self).__init__(*args, **kwargs)
        self.fields['approved_mission'].label = 'How would you like to display this mission?'
    class Meta:
        """set up our form fields"""
        model = Mission
        fields = [
            'approved_mission'
        ]
        widgets = {
            'approved_mission': forms.Select(
                attrs={
                    'style': 'width: 100%;',
                }
            )
        }


class UpdateForm(forms.ModelForm):
    """Set up form for writing an update"""
    def __init__(self, *args, **kwargs):
        super(UpdateForm, self).__init__(*args, **kwargs)
        self.fields['body'].label = 'Update Contents'
    class Meta:
        """update meta for Update form"""
        model = Update
        fields = [
            'title',
            'body'
        ]
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'placeholder': 'Update title here'
                }
            ),
            'body': forms.Textarea(
                attrs={
                    'placeholder': 'Add Update Contents Here'
                }
            ),
        }


class ApproveUpdateForm(forms.ModelForm):
    """set up a new form for approving updates"""
    def __init__(self, *args, **kwargs):
        super(ApproveUpdateForm, self).__init__(*args, **kwargs)
        self.fields['approved'].label = 'How would you like to display this update?'
    class Meta:
        """set up our form fields"""
        model = Update
        fields = [
            'approved'
        ]
        widgets = {
            'approved': forms.Select(
                attrs={
                    'style': 'width: 100%;',
                }
            )
        }
