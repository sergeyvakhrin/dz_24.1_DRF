from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):

        # test1 = User.objects.get(email='test1@test1.ru')
        # test1.set_password('1234')
        # test1.save()
        #
        # test2 = User.objects.get(email='test2@test2.ru')
        # test2.set_password('1234')
        # test2.save()
        #
        # test3 = User.objects.get(email='test3@test3.ru')
        # test3.set_password('1234')
        # test3.save()

        user = User.objects.create(
            email='admin@sky.pro',
            first_name='Admin',
            last_name='SkyPro',
            is_staff=True,
            is_superuser=True,
        )

        user.set_password('1234')
        user.save()
