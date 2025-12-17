from django.conf import settings
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    following = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        symmetrical=False,
        related_name='followers',
        blank=True
    )

    def __str__(self):
        return self.user.username

