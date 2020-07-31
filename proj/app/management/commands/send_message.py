from django.core.management.base import BaseCommand
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('cmd')
    def handle(self, *args, **options):
        async_to_sync(get_channel_layer().send)(options["cmd"], {"type": "test.print", "text": "fnord"})
