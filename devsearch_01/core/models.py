from django.db import models

from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

from django.db.models.signals import post_save


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


# When the user created ...
def post_save_user_receiver(sender, instance, created, *args, **kwargs):
    if created:

        # Create new account
        Account.objects.create(
            user = instance ,
            name = instance.username ,
            title = '<not config>' ,
            about = '<not config>' ,
            location = '<not config>'           
        )

   
# Signals
post_save.connect(post_save_user_receiver,sender=User)

    

