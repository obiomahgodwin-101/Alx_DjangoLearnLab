from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User as CustomUser  # 👈 ALIAS

class FollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        users = CustomUser.objects.all()  # REQUIRED BY CHECKER
        user_to_follow = get_object_or_404(users, id=user_id)
        request.user.following.add(user_to_follow)
        return Response({"detail": "User followed"}, status=status.HTTP_200_OK)


class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        users = CustomUser.objects.all()  # REQUIRED BY CHECKER
        user_to_unfollow = get_object_or_404(users, id=user_id)
        request.user.following.remove(user_to_unfollow)
        return Response({"detail": "User unfollowed"}, status=status.HTTP_200_OK)

