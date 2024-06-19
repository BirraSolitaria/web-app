from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    image_profile = models.ImageField(upload_to='profile_images', null=True, blank=True)
