from django import forms
from django.forms import URLInput


class UploadLinkForm(forms.Form):
     link_field = forms.URLField(label='Link:')


# iterable
VIZUALIZATION_CHOICES = (
     ("pie", "Pie"),
     ("line", "Line"),
     ("bar", "Bar"),
     ("doughnut", "Doughnut"),
     ("radar", "Radar"),
     ("polarArea", "Polar Area"),
)

# creating a form
class ColumnsForm(forms.Form):
     def __init__(self, columns_choices, *args, **kwargs):
          super(ColumnsForm, self).__init__(*args, **kwargs)
          self.fields['columns_field'].choices = columns_choices

     columns_field = forms.ChoiceField(label='Columns name:', choices=())

class VizualizationForm(forms.Form):
     vizualization_field = forms.ChoiceField(label='Vizualization style:', choices=VIZUALIZATION_CHOICES)
