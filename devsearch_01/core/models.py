from django.db import models
from django.conf import settings

from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

from django.db.models.signals import post_save

# Pillow
from PIL import Image as TheImage


def get_image_location(instance, file_name):
    return f"account_profile_image/{instance.pk}/{file_name}"

def get_default_image_path():
    return f"account_profile_image/default/default.png"


def get_project_image_location(instance, file_name):
    return f"profile_image/{instance.pk}/{file_name}"

def get_default_project_image_path():
    return f"project_image/default/default.png"

def crop_image(image, size):
    # Open the image using Pillow
    img = TheImage.open(image)
    
    # Calculate the aspect ratio of the original image
    aspect_ratio = img.width / img.height
    
    # Calculate the target width and height based on the desired size and aspect ratio
    target_width = size[0]
    target_height = int(target_width / aspect_ratio)
    
    # Resize the image maintaining the aspect ratio
    img.thumbnail((target_width, target_height), TheImage.ANTIALIAS)
    
    # Calculate the cropping position based on the resized image dimensions
    left = (img.width - size[0]) / 2
    top = (img.height - size[1]) / 2
    right = (img.width + size[0]) / 2
    bottom = (img.height + size[1]) / 2
    
    # Crop the resized image
    img = img.crop((left, top, right, bottom))
    
    # Save the cropped and resized image
    img.save(image.path)
    
    print('image.path: ', image.path)
    print('image.url: ', image.url)




class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=250, null=True, blank=True)
    title = models.CharField(max_length=250, null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    profile_image = models.ImageField(upload_to=get_image_location, default=get_default_image_path)
    location = models.CharField(max_length=250, null=True, blank=True)

    def save(self, *args, **kwargs):
        # Call the parent save() method to ensure other model operations are performed
        super().save(*args, **kwargs)
        
        # Specify the desired size for cropping
        crop_size = (600 , 600)  # Adjust as per your requirements
        
        # Call the crop_image method to crop the uploaded image
        crop_image(self.profile_image, crop_size)

    def __str__(self) -> str:
        return f"Account -- > {self.user.username}"

class Skill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)

class Tool(models.Model):
    project = models.ForeignKey('Project', on_delete=models.CASCADE)
    tool = models.CharField(max_length=250)

class Image(models.Model):
    file = models.ImageField(verbose_name='Project Image', upload_to=get_project_image_location, default=get_default_project_image_path)

    def save(self, *args, **kwargs):
        # Call the parent save() method to ensure other model operations are performed
        super().save(*args, **kwargs)
        
        # Specify the desired size for cropping
        crop_size = (1024, 768)  # Adjust as per your requirements
        
        # Call the crop_image method to crop the uploaded image
        crop_image(self.file, crop_size)

class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image_project = models.ManyToManyField('Image', blank=True)
    title = models.CharField(max_length=250, blank=True, null=True, default='Blank')
    about = models.TextField(blank=True, null=True)
    link = models.URLField(help_text="a link the deployed project", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        if not self.link:  # If link field is empty
            self.link = f"{settings.DOMAIN}/project/{self.pk}/"  # Set a default link
            print('self.pk: ', self.pk)
        super().save(*args, **kwargs)



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

    

