from django import forms
from django.forms import Select

from .models import News
from missions.widgets import CustomClearableFileInput

TYPES = ((1, 'General'), (2, 'Systems'), (3, 'Discoveries'))

class NewsForm(forms.ModelForm):
    """Set up the news form for new content"""
    class Meta:
        """set up for our widgets"""
        model = News
        fields = [
            'title',
            'news_type',
            'news_img',
            'news_content',
            'approved_post',
        ]
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'placeholder': 'Article Title Here'
                }
            ),
            'news_type': forms.RadioSelect(),
            'news_content': forms.Textarea(
                attrs={
                    'placeholder': 'Add title Content Here'
                }
            ),
            'approved_post': forms.Select(
                attrs={
                    'style': 'width: 200px;',
                }
            )
        }

    news_img = forms.ImageField(
        label='Image Upload',
        required=False,
        widget=CustomClearableFileInput,
    )


class ApproveNewsForm(forms.ModelForm):
    """set up our approval form for news articles"""
    def __init__(self, *args, **kwargs):
        super(ApproveNewsForm, self).__init__(*args, **kwargs)
        self.fields['approved_post'].label = 'How would you like to display this article?'
    class Meta:
        """Add form elements"""
        model = News
        fields = [
            'approved_post'
        ]
        widgets = {
            'approved_post': forms.Select(
                attrs={
                    'style': 'width: 100%;',
                }
            )
        }
