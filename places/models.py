from django.db import models

# Create your models here.


class Place(models.Model):
    title = models.CharField(max_length=50)
    description_short = models.CharField(max_length=255)
    description_long = models.TextField()

    def __str__(self):
        return self.title
