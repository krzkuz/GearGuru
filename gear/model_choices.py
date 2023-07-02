from django.db import models


class PickupConfigurationChoices(models.TextChoices):
    H = 'H', 'Humbucker'
    HH = 'HH', 'Two humbuckers'
    HHH = 'HHH', 'Three humbuckers'
    S = 'S', 'Singlecoil'
    SS = 'SS', 'Two singlecoils'
    SSS = 'SSS', 'Three singlecoils'
    HS = 'HS', 'Humbucker + Singlecoil'
    HSS = 'HSS', 'Humbucker + two singlecoils'
    OTHER = 'OTH', 'Other'
    NONE = 'NON', 'No pickups'


class GuitarTypeChoices(models.TextChoices):
    CLASSICAL = 'CL', 'Classical'
    ELECTRIC = 'EL', 'Electric'
    ACOUSTIC = 'AC', 'Acoustic'
    BASS = 'BA', 'Bass'


class BridgeTypeChoices(models.TextChoices):
    FIXED = 'FI', 'Fixed bridge'
    TREMOLO = 'TR', 'Tremolo bridge'


class BodyTypeChoices(models.TextChoices):
    SEMI = 'SE', 'Semi hollow body'
    HOLLOW = 'HO', 'Hollow body'
    SOLID = 'SO', 'Solid body'


class ConditionTypeChoices(models.TextChoices):
    EXCELLENT = 'EXC', 'Excellent condition'
    VERY_GOOD = 'VGO', 'Very good condition'
    GOOD = 'GOO', 'Good condition'
    FAIR = 'FAI', 'Fair condition'
    POOR = 'POR', 'Poor condition'


class TransactionTypeChoices(models.TextChoices):
    SELL = 'SEL', 'Sell'
    EXCHANGE = 'EXC', 'Exchange'
    RENT = 'REN', 'Rent'
