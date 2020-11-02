from django.db import models
from django_prometheus.models import ExportModelOperationsMixin


# Create your models here.
class Visit(ExportModelOperationsMixin('visit'), models.Model):
    ip = models.GenericIPAddressField(unique=True)
    last_visit = models.DateTimeField()
    visits = models.IntegerField()
