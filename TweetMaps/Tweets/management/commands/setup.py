from django.core.management.base import BaseCommand
from django.core.management import call_command
import os
from pathlib import Path



class Command(BaseCommand):
    help = 'Sets up the system'

    def handle(self, *args, **kwargs):
        if os.path.exists('/TweetMaps/Tweets/migrations'):
            call_command("migrate","Tweets","zero")
        call_command("migrate")
        call_command("makemigrations", "Tweets")
        call_command("migrate","Tweets")
