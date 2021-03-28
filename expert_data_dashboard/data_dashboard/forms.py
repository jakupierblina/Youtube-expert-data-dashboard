from django import forms
from django.forms import URLInput


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
