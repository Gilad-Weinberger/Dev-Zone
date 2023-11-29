from django.db import models

class Class(models.Model):
    name = models.CharField(max_length=8, null=True, blank=True)