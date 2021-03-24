from django.db import models
from django.db.models import Model
# Create your models here.

# Create your models here.

class UploadLinkModel(Model):
      link_field = models.URLField(max_length=200)
