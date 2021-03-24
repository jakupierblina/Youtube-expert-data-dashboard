from django import forms
from django.forms import URLInput


class UploadLinkForm(forms.Form):
     link_field =  forms.URLField(label='Link:')




# iterable
GEEKS_CHOICES = (
     ("1", "One"),
     ("2", "Two"),
     ("3", "Three"),
     ("4", "Four"),
     ("5", "Five"),
)

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
     columns_field = forms.ChoiceField(choices=GEEKS_CHOICES)
     vizualization_field = forms.ChoiceField(choices=VIZUALIZATION_CHOICES)
