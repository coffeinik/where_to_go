from django.shortcuts import render
from django.urls import reverse
from geojson import FeatureCollection, Feature, Point

from places.models import Place

def index(request):
    places: Place = Place.objects.all()
    feature_collection = FeatureCollection(features=[
        Feature(
            geometry=Point((place.coordinates_lng, place.coordinates_lat)),
            properties={
                'title': place.title,
                'placeId': place.id,
                'detailsUrl': reverse(index) # TODO
            })
        for place in places]
    )
    return render(request, 'index.html', context={'feature_collection': feature_collection})
