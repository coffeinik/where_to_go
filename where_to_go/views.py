from django.shortcuts import render
from geojson import FeatureCollection, Feature, Point


def index(request):
    feature_collection = FeatureCollection(features=[
        Feature(geometry=Point((37.62, 55.793676)), properties={
            'title': '«Легенды Москвы',
            'placeId': 'moscow_legends',
            'detailsUrl': 'https://raw.githubusercontent.com/devmanorg/where-to-go-frontend/master/places/moscow_legends.json'
          }),
        Feature(geometry=Point((37.64, 55.753676)), properties={
            'title': 'Крыши24.рф',
            'placeId': 'roofs24',
            'detailsUrl': 'https://raw.githubusercontent.com/devmanorg/where-to-go-frontend/master/places/roofs24.json'
          }
        )
    ])
    return render(request, 'index.html', context={'feature_collection': feature_collection})
