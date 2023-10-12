from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_phone_number': 'Phone Number',
            'default_town_or_city': 'Town or City',
            'default_county': 'County or State',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_postcode': 'Postcode',
        }
        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = (
                'w-75'
                )
        self.fields['default_phone_number'].label = 'Phone Number:'
        self.fields['default_town_or_city'].label = 'Town or City:'
        self.fields['default_country'].label = 'Country:'
