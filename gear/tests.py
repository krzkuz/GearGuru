from django.test import TestCase

from .models import Guitar
from users.models import CustomUser
from .model_choices import (TransactionTypeChoices, GuitarTypeChoices, 
    ConditionTypeChoices, PickupConfigurationChoices, BridgeTypeChoices)


class GuitarModelTestCase(TestCase):
    def create_user(self):
        self.user = CustomUser.objects.create(
            username='qwe',
            email='qwe@gmail.com',
            password='Password123',
        )

    def create_guitar(self):
        self.guitar_a = Guitar.objects.create(
            brand='Fender',
            model='Duo Sonic',
            transaction_type=TransactionTypeChoices.SELL,
            guitar_type=GuitarTypeChoices.ELECTRIC,
            condition=ConditionTypeChoices.VERY_GOOD,
            number_of_strings=6,
            pickup_configuration=PickupConfigurationChoices.HS,
            bridge_type=BridgeTypeChoices.FIXED,
            owner=self.user
        )

        self.guitar_b = Guitar.objects.create(
            brand='Fender',
            model='Precision Bass',
            transaction_type=TransactionTypeChoices.SELL,
            guitar_type=GuitarTypeChoices.BASS,
            condition=ConditionTypeChoices.VERY_GOOD,
            number_of_strings=4,
            pickup_configuration=PickupConfigurationChoices.S,
            bridge_type=BridgeTypeChoices.FIXED,
            owner=self.user
        )

    def setUp(self):
        self.create_user()
        self.create_guitar()

    def test_is_user_created(self):
        qs = CustomUser.objects.all()
        self.assertEqual(qs.count(), 1)

    def test_are_guitar_created(self):
        qs = Guitar.objects.all()
        self.assertEqual(qs.count(), 2)

    def test_electric_guitar_exists(self):
        qs = Guitar.objects.filter(guitar_type=GuitarTypeChoices.ELECTRIC)
        self.assertTrue(qs.exists())

    def test_guitar_owner(self):
        owner = self.guitar_a.owner
        self.assertEqual(owner, self.user)

    def test_guitar_brand(self):
        brand = self.guitar_a.brand
        self.assertEqual(brand, 'Fender')

    def test_owner_guitars_count(self):
        user_guitars = self.user.guitar_set.all()
        self.assertEqual(user_guitars.count(), 2)