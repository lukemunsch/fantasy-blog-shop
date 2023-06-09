from django import forms

from .models import News
from .widgets import CustomClearableFileInput

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
        }

    news_img = forms.ImageField(
        label='Image Upload',
        required=False,
        widget=CustomClearableFileInput,
    )
