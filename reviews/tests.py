from django.test import TestCase

from .models import Review
from users.models import CustomUser


class ReviewModelTestCase(TestCase):
    
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

        self.review = Review.objects.create(
            rate='5',
            from_user=self.user_a,
            to_user=self.user_b,
        )

    def test_users_created(self):
        qs = CustomUser.objects.all()
        self.assertEqual(qs.count(), 2)

    def test_review_created(self):
        qs = Review.objects.all()
        self.assertTrue(qs.exists())

    def test_from_user(self):
        from_user = self.review.from_user
        self.assertEqual(from_user, self.user_a)

    def test_to_user(self):
        to_user = self.review.to_user
        self.assertEqual(to_user, self.user_b)