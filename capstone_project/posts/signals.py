from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Like
from notifications.models import Notification

@receiver(post_save, sender=Like)
def create_like_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            user=instance.post.author,  # the post's author
            message=f"{instance.user.username} liked your post.",
            post=instance.post
        )

