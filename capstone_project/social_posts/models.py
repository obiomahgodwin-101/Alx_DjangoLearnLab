from django.contrib.auth import get_user_model
User = get_user_model()

class Like(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="likes"
    )
    post = models.ForeignKey(
        'Post',
        on_delete=models.CASCADE,
        related_name="likes"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'post')  # Prevents duplicate likes

    def __str__(self):
        return f"{self.user.username} liked Post {self.post.id}"

