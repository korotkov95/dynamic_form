from django.db import models
from django.contrib.postgres.fields import JSONField

# Create your models here.
class NameData(models.Model):
	data = JSONField()