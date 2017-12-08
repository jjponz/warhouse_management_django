from django.db import models
from django.utils import timezone

class Item(models.Model):
    _name = models.CharField(default="", max_length=255, db_column="name")
    _notes = models.CharField(default="", max_length=1000, db_column="notes")
    _creation_date = models.DateField(default=timezone.now, db_column="creation_date")
