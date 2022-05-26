from distutils.command.upload import upload
from email.policy import default
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='profile_pic.jpeg',upload_to="Profile_pic")
    Location = models.CharField(max_length=200)

    def __str__(self):
        return self.user.username
