from django.db import models


# Create your models here.
class Visit(models.Model):
    ip = models.TextField(unique=True)
    last_visit = models.DateTimeField()
