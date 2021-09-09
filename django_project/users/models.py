from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  image = models.ImageField(default='default.jpg', upload_to='profile_pics')

  def __str__(self):
    return f'{self.user.username} Profile'

  """ 
  The function bellow is to resize and save images using pillow library. 
  We commented the code because there is some steps to use this with aws s3, so we are not using it for the moment
  def save(self, *args, **kwargs):
    super().save(*args, **kwargs) # override save method of a model

    img = Image.open(self.image.path)

    if img.height > 300 or img.width > 300:
      output_size = (300, 300)
      img.thumbnail(output_size)
      img.save(self.image.path)
 """
