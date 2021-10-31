from django.db import models

class Audio(models.Model):
    title = models.CharField(max_length=200)
    language = models.CharField(max_length=100)
    good_quality = models.BooleanField()

    def __str__(self):
        return self.title

