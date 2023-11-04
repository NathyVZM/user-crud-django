from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email field it\'s required')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('superusuario required is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('superusuario required is_superuser=True.')

        return self.create_user(email, password=password, **extra_fields)

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(blank=True, max_length=20)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    # set User Manager
    objects = UserManager()