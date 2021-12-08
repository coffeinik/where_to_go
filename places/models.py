from django.db import models

# Create your models here.


class Place(models.Model):
    title = models.CharField(max_length=50)
    description_short = models.CharField(max_length=255)
    description_long = models.TextField()

    def __str__(self):
        return self.title


class PlaceImage(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    image = models.ImageField()
    order_number = models.IntegerField()

    def __str__(self):
        return self.image.name
