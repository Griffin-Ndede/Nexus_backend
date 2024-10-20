from django.db import models
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
import os

class Video(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    video_file = models.FileField(upload_to='videos/')
    cover_image = models.ImageField(upload_to='covers/', blank=True, null=True) 
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

def upload_to(instance, filename):
    # Determine the path based on the model class
    if isinstance(instance, Categories):
        return f'category_images/{filename}'

@deconstructible
class ValidateImageFileExtension(object):
    valid_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']

    def __call__(self, value):
        ext = os.path.splitext(value.name)[1]
        if ext.lower() not in self.valid_extensions:
            raise ValidationError(f'Unsupported file extension. Supported extensions are: {", ".join(self.valid_extensions)}')


class Categories(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to=upload_to, null=True, validators=[ValidateImageFileExtension()])
    
    def __str__(self):
        return self.title