from screenshot.tasks import scan, load_status_imgs
from django.core.management.base import BaseCommand


load_status_imgs('./screenshot/status')


class Command(BaseCommand):
    def handle(self, *args, **options):
        scan()
