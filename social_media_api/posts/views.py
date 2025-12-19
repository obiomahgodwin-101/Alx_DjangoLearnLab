from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Post, Like
from .serializers import PostSerializer


class FeedView(generics.ListAPIView):
    """
    Returns posts from users that the current user follows,
    ordered by most recent first.
    """
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        following_users = user.following.all()
        return Post.objects.filter(author__in=following_users).order_by('-created_at')


class LikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, post_id):
        post = Post.objects.get(id=post_id)
        Like.objects.get_or_create(user=request.user, post=post)
        return Response({"message": "Post liked"}, status=status.HTTP_200_OK)


class UnlikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, post_id):
        Like.objects.filter(user=request.user, post_id=post_id).delete()
        return Response({"message": "Post unliked"}, status=status.HTTP_200_OK)

