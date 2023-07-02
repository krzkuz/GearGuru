from django.test import TestCase
from .models import CustomUser


class UserModelTestCase(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create(
            username='qwe',
            email='qwe@gmail.com',
            password='Password123',
            first_name='qwerty',
            last_name='uiop',
            country='Poland',
            city='Łódź',
            street='Piotrkowska',
            apartment='80/40a',
            zip_code='90-000'
        )

    def test_is_user_created(self):
        qs = CustomUser.objects.all()
        self.assertTrue(qs.exists())

    def test_is_not_staff(self):
        qs = CustomUser.objects.filter(is_staff=False)
        self.assertEqual(qs.count(), 1)

    def test_username(self):
        self.assertEqual(self.user.username, 'qwe')

    def test_user_country(self):
        self.assertEqual(self.user.country, 'Poland')
