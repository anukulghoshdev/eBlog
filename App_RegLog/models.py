from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# User Model -> username password email first_name last_name

class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='userinfo')

    facebook_id = models.URLField(blank=True)

    profile_pic = models.ImageField(upload_to = 'profile_pics', blank=True)
