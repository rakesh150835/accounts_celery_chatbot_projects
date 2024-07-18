from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver
from .models import Profile, User
import os


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


# remove previous profile picture when new image is uploaded
@receiver(pre_save, sender=Profile)
def delete_old_image_on_update(sender, instance, **kwargs):

    try:
        old_file = Profile.objects.get(pk=instance.pk).image
    except Profile.DoesNotExist:
        return False

    new_file = instance.image
    if old_file != new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)

            
# remove profile picture when profile get deleted
@receiver(post_delete, sender=Profile)
def delete_profile_image(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)