from django.db.models.signals import post_save
from django.dispatch import receiver

from profiles.models import UserProfile, Addresses, UserSocialMedia
from accounts.models import User


@receiver(post_save, sender=User)
def create_profiles(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def create_addresses(sender, instance, created, **kwargs):
    if created:
        Addresses.objects.create(user=instance)
