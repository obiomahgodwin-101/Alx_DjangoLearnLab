from django.db.models.signals import post_save
from django.dispatch import receiver
from posts.models import Like
from .models import Notification


@receiver(post_save, sender=Like)
def create_like_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            user=instance.post.author,
            message=f"{instance.user.username} liked your post",
            post=instance.post
        )

