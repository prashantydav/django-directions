from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile

@receiver(post_save , sender = User)
def create_profile(created , instance , sender , **kwargs):
    if created:
        return UserProfile.objects.create(user = instance)
