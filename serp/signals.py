from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import UserConfig


@receiver(post_save, sender=User)
def create_user_config(sender, instance, created, **kwargs):
    if created:
        UserConfig.objects.create(user=instance)
