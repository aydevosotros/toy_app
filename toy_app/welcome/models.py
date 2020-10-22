from django.db import models


# Create your models here.
class Visit(models.Model):
    ip = models.GenericIPAddressField(unique=True)
    last_visit = models.DateTimeField()
    visits = models.IntegerField()
