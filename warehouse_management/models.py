from django.db import models

class ItemMapper(models.Model):
    name = models.CharField(default="", max_length=255)
    notes = models.CharField(default="", max_length=1000)
    uid = models.CharField(max_length=100, primary_key=True)
