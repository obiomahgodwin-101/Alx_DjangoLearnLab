from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

from posts.models import Like
from notifications.models import Notification

User = get_user_model()


@receiver(post_save, sender=Like)
def create_notification_on_like(sender, instance, created, **kwargs):
    """
    Create notification when a post is liked
    """
    if not created:
        return

    post = instance.post
    sender_user = instance.user
    receiver_user = post.author

    # Don't notify if user likes their own post
    if sender_user == receiver_user:
        return

    Notification.objects.create(
        user=receiver_user,
        actor=sender_user,
        verb="liked your post",
        target=post
    )

