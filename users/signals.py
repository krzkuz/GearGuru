from django.db.models.signals import post_save

from reviews.models import Review


def review_about_user(sender, instance, created, **kwargs):
    if created:
        user = instance.to_user
        user_ratings = Review.objects.filter(to_user=user)
        sum = 0
        for obj in user_ratings:
            sum += int(obj.rate)
        user.average_rating = sum / user_ratings.count()
        user.save()

post_save.connect(review_about_user, sender=Review)