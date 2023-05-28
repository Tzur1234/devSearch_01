from django.db import models

from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


def get_image_location(instance, file_name):
    return f"account_profile_image/{instance.pk}/{file_name}"

def get_default_image_path():
    return f"account_profile_image/default/default.png"


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=250, null=True, blank=True)
    title = models.CharField(max_length=250, null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    profile_image = models.ImageField(upload_to=get_image_location, default=get_default_image_path)
    location = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self) -> str:
        return f"Account -- > {self.user.username}"

class Skill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)

    

