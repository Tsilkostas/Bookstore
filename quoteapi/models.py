from django.db import models

# Create your models here.

class Quotes(models.Model):
    content = models.CharField(max_length=300)
    originator = models.CharField(max_length=100, blank=True)
    url = models.CharField(max_length=100, blank=True)
    tag = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name