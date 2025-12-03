from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

ROLE_CHOICES = (
    ('Admin', 'Admin'),
    ('Librarian', 'Librarian'),
    ('Member', 'Member'),
)

# ----------------------------------
# Custom User Manager
# ----------------------------------
class CustomUserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Users must have an email address")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)


# ----------------------------------
# Custom User Model
# ----------------------------------
class CustomUser(AbstractUser):
    username = None  # removing username (we use email instead)
    email = models.EmailField(unique=True)
    
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Member')

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # removes need for username

    def __str__(self):
        return self.email

