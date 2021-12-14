import logging
from io import BytesIO

import requests
from requests.exceptions import RequestException
from django.core.management.base import BaseCommand

from places.models import Place, PlaceImage

logger = logging.getLogger('main')


class Command(BaseCommand):
    help = 'Load places to database from JSON by url'

    def add_arguments(self, parser):
        parser.add_argument('url', type=str)

    def handle(self, *args, **options):
        try:            
            data = requests.get(options.get('url')).json()
        except RequestException as e:
            logger.error(e)
            return
        defaults = {
            'description_short': data['description_short'],
            'description_long': data['description_long'],
            'coordinates_lng': data['coordinates']['lng'],
            'coordinates_lat': data['coordinates']['lat']
        }
        place, created = Place.objects.get_or_create(
            title=data['title'], defaults=defaults
        )
        if created:
            images_paths = data['imgs']
            for order_number, image_path in enumerate(images_paths):
                r = requests.get(image_path)
                place_image = PlaceImage(place=place, order_number=order_number)
                place_image.image.save(f'{place.id}_{order_number}.jpg', BytesIO(r.content))
            print(f'Finished loading place "{place.title}"')
        else:
            print(f'Place "{place.title}" is already uploaded')
