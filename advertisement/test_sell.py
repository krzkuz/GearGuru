from django.test import TestCase

from .models import Sell
from users.models import CustomUser
from gear.models import Guitar
from gear.model_choices import TransactionTypeChoices, GuitarTypeChoices,ConditionTypeChoices


class SellTestCase(TestCase):
    def create_owner(self):
        self.owner = CustomUser.objects.create(
            username='qwe',
            email='qwe@gmail.com',
            password='Password123',
        )

    def create_guitar(self):
        self.guitar_a = Guitar.objects.create(
            brand='Epiphone',
            model='CASINO',
            transaction_type=TransactionTypeChoices.SELL,
            guitar_type=GuitarTypeChoices.ELECTRIC,
            condition=ConditionTypeChoices.VERY_GOOD,
            owner=self.owner
        )
        self.guitar_b = Guitar.objects.create(
            brand='Gretsch',
            model='corvette',
            transaction_type=TransactionTypeChoices.SELL,
            guitar_type=GuitarTypeChoices.ELECTRIC,
            condition=ConditionTypeChoices.EXCELLENT,
            owner=self.owner
        )
        self.guitar_c = Guitar.objects.create(
            brand='Yamaha',
            model='F310',
            transaction_type=TransactionTypeChoices.SELL,
            guitar_type=GuitarTypeChoices.ACOUSTIC,
            condition=ConditionTypeChoices.FAIR,
            owner=self.owner
        )    

    def create_advertisements(self):
        self.ad_1 = Sell.objects.get(related_gear=self.guitar_a)
        self.ad_1.title = 'Guitar for sell'
        self.ad_1.price = 100
        self.ad_1.more_info = 'Looks like new'

        self.ad_2 = Sell.objects.get(related_gear=self.guitar_b)
        self.ad_2.title = 'Guitar for sell 2'
        self.ad_2.price = 200
        self.ad_2.more_info = 'Looks like new 2'

        self.ad_3 = Sell.objects.get(related_gear=self.guitar_c)
        self.ad_3.title = 'Guitar for sell 3'
        self.ad_3.price = 300
        self.ad_3.more_info = 'Looks like new 3'

    def setUp(self):
        self.create_owner()
        self.create_guitar()
        self.create_advertisements()

    def test_advertisements_created(self):
        ads = Sell.objects.all()
        self.assertEqual(ads.count(), 3)