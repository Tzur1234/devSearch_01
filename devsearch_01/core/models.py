from django.db import models

from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


def get_image_location(instance, file_name):
    return f"account_profile_image/{instance.id}/{file_name}"

def get_default_image_path():
    return f"account_profile_image/default/default.img"


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about = models.TextField()
    profile_image = models.ImageField(upload_to=get_image_location, default=get_default_image_path)
    location = models.CharField(max_length=250)

