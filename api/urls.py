from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthorList, BookViewSet

# Create DRF router and register BookViewSet
router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')

urlpatterns = [
    # List view for authors
    path('authors/', AuthorList.as_view(), name='author-list'),

    # Include all router URLs for Book CRUD
    path('', include(router.urls)),
]

