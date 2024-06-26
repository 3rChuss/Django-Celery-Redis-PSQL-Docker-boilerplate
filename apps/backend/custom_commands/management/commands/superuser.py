from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model
from decouple import config

DJANGO_SUPERUSER_USERNAME = config('DJANGO_SUPERUSER_USERNAME', cast=str)
DJANGO_SUPERUSER_EMAIL = config('DJANGO_SUPERUSER_EMAIL', cast=str)
DJANGO_SUPERUSER_PASSWORD = config('DJANGO_SUPERUSER_PASSWORD', cast=str)

class Command(BaseCommand):
    help = 'Create a superuser with the provided credentials'

    def handle(self, *args, **options):
        try:
            User = get_user_model()
            if User.objects.filter(username=DJANGO_SUPERUSER_USERNAME).exists():
                raise CommandError('Superuser already exists')
            user = User.objects.create_superuser(
                username=DJANGO_SUPERUSER_USERNAME,
                email=DJANGO_SUPERUSER_EMAIL,
            )
            user.set_password(DJANGO_SUPERUSER_PASSWORD)
            user.is_active = True
            user.is_staff = True
            user.is_superuser = True
            user.is_admin = True
            user.save()

            self.stdout.write(self.style.SUCCESS('Superuser created successfully'))
        
        except Exception as e:
            raise CommandError(e)
        

