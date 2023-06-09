from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _


class CustomClearableFileInput(ClearableFileInput):
    clear_checkbox_label = _('Remove Image')

    initial_text = ('Current Image')
    input_text = ('')
    template_name = (
        'missions/custom_widget_template/custom_clearable_file_input.html'
    )
