from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

User = get_user_model()

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def follow_user(request, user_id):
    target_user = get_object_or_404(User, id=user_id)
    profile = request.user.profile
    if target_user != request.user:
        profile.following.add(target_user)
    return Response({'message': f'You are now following {target_user.username}'}, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unfollow_user(request, user_id):
    target_user = get_object_or_404(User, id=user_id)
    profile = request.user.profile
    if target_user != request.user:
        profile.following.remove(target_user)
    return Response({'message': f'You have unfollowed {target_user.username}'}, status=status.HTTP_200_OK)

