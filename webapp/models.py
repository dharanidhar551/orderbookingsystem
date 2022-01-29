from django.db import models
from datetime import datetime
# Create your models here.

class Uploadcsv(models.Model):
    title=models.CharField(max_length=100)
    file=models.FileField(upload_to="CSV/")
    def __str__(self):
        return self.title