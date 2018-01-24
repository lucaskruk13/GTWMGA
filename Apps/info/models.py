from django.db import models

class ByLaw(models.Model):
    bylaws = models.TextField(blank=False, null=False)

