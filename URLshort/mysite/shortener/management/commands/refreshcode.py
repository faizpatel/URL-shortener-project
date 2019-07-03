from django.core.management.base import BaseCommand, CommandError
from shortener.models import shortURL

class Command(BaseCommand):
    help = 'Refreshs shortcode for URL'

    def add_arguments(self, parser):
        parser.add_argument('items', type=int)

    def handle(self, *args, **options):
        return shortURL.objects.refresh_shortcode(items=options['items'])
