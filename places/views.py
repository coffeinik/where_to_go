from django.http import JsonResponse

from .models import Place


def get_place(request, place_id):
    place = Place.objects.get(pk=place_id)
    place_json = {
        "title": place.title,
        "imgs": [image.image.url for image in place.images.all()],
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lat": place.coordinates_lat,
            "lng": place.coordinates_lng
        }
    }
    return JsonResponse(place_json, safe=False, json_dumps_params={'ensure_ascii': False})
