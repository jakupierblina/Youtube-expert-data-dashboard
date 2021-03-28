from _ast import arg

from django import forms
from django.forms import URLInput
from . import views

class UploadLinkForm(forms.Form):
     link_field =  forms.URLField(label='Link:')


# iterable
COLUMNS_CHOICES = (
     ("one", "One"),
     ("two", "Two"),
     ("three", "Three"),
     ("four", "Four"),
)

VIZUALIZATION_CHOICES = (
     ("line", "Line"),
     ("bar", "Bar"),
     ("pie", "Pie"),
     ("doughnut", "Doughnut"),
     ("radar", "Radar"),
     ("polarArea", "Polar Area"),
)


# creating a form
class ColumnsForm(forms.Form):
     columns_field = forms.ChoiceField(label='Columns name:', choices=COLUMNS_CHOICES)
     vizualization_field = forms.ChoiceField(label='Vizualization style:', choices=VIZUALIZATION_CHOICES)

     def __init__(self, *args, **kwargs):
          super(ColumnsForm, self).__init__(*arg, **kwargs)

          # get the choices from where you need
          choices = ()
          self.fields['vote'].choices = choices
