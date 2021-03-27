from django.db import models
from django.db.models import Model
# Create your models here.

# Create your models here.

class UploadLinkModel(Model):
      link_field = models.URLField(max_length=200)


# iterable
GEEKS_CHOICES = (
     ("1", "One"),
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

class ColumnsModel(models.Model):
      columns_field = models.CharField(max_length=100, blank=True, choices=GEEKS_CHOICES)
      vizualization_field = models.CharField(max_length=100, blank=True, choices=VIZUALIZATION_CHOICES)