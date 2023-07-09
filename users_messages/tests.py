from django.test import TestCase
from django.core.files.images import ImageFile

from .models import Message, Image
from users.models import CustomUser

from django.core.files.uploadedfile import SimpleUploadedFile

class MessageTestCase(TestCase):
    def create_users(self):
        self.user_a = CustomUser.objects.create(
            username='qwe',
            email='qwe@gmail.com',
            password='Password123',
        )

        self.user_b = CustomUser.objects.create(
            username='qwerty',
            email='qwerty@gmail.com',
            password='Password123',
        )

    def setUp(self):
        self.create_users()
        self.image_file = SimpleUploadedFile(
            '/static/images/Gibson-Custom.jpg',
            b'file_content',
            content_type='image/jpeg'
        )

        self.message = Message.objects.create(
            title='abc',
            from_user=self.user_a,
            to_user=self.user_b
        )

        self.image = Image.objects.create(
            image=self.image_file,
            message = self.message
            )

    def test_is_image_created(self):
        qs = Image.objects.all()
        self.assertTrue(qs.count(), 1)