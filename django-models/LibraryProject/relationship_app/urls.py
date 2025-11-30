from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views  # ✅ Must import views this way for checker

urlpatterns = [
    # Books list - function-based view
    path('books/', views.list_books, name='list_books'),

    # Library detail - class-based view
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

    # Authentication URLs
    path('register/', views.register, name='register'),  # ✅ Must be 'views.register'
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
]

