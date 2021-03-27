from django import forms
from django.forms import URLInput


class UploadLinkForm(forms.Form):
     link_field =  forms.URLField(label='Link:')


# iterable
COLUMNS_CHOICES = ( )

VIZUALIZATION_CHOICES = (
     ("line", "Line"),
     ("bar", "Bar"),
     ("pie", "Pie"),
     ("doughnut", "Doughnut"),
     ("radar", "Radar"),
     ("polar", "Polar Area"),
     ("bubble", "Bubble"),
     ("scatter", "Scatter "),
)


# creating a form
class ColumnsForm(forms.Form):
     columns_field = forms.ChoiceField(choices=COLUMNS_CHOICES)
     vizualization_field = forms.ChoiceField(choices=VIZUALIZATION_CHOICES)
