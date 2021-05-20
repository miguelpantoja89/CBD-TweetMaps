from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.contrib.auth.models import Group


class Command(BaseCommand):
    help = 'Creates admin user'

    def handle(self, *args, **kwargs):
        User.objects.create_superuser('admin', 'admin@example.com', 'pass')