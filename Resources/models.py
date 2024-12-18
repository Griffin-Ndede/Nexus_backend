from django.db import models
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from cloudinary.models import CloudinaryField
import os

# Base model for shared fields
class BaseVideo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    # Specify folder for videos
    video_file = CloudinaryField('video', resource_type='video', folder='videos')  
    # Specify folder for cover images
    cover_image = CloudinaryField('image', folder='cover_images', null=True)  
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True  # Ensure this model is not created as a database table

    def __str__(self):
        return self.title

# Separate models for each form level
class Form1Video(BaseVideo):
    class Meta:
        verbose_name = "Form 1 Video"
        verbose_name_plural = "Form 1 Videos"

class Form2Video(BaseVideo):
    class Meta:
        verbose_name = "Form 2 Video"
        verbose_name_plural = "Form 2 Videos"

class Form3Video(BaseVideo):
    class Meta:
        verbose_name = "Form 3 Video"
        verbose_name_plural = "Form 3 Videos"

class Form4Video(BaseVideo):
    class Meta:
        verbose_name = "Form 4 Video"
        verbose_name_plural = "Form 4 Videos"

# Image file extension validator
@deconstructible
class ValidateImageFileExtension:
    valid_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']

    def __call__(self, value):
        ext = os.path.splitext(value.name)[1]
        if ext.lower() not in self.valid_extensions:
            raise ValidationError(f'Unsupported file extension. Supported extensions are: {", ".join(self.valid_extensions)}')

class Categories(models.Model):
    title = models.CharField(max_length=100)
    # Specify folder for category images
    image = CloudinaryField('image', folder='category_images', validators=[ValidateImageFileExtension()])

    def __str__(self):
        return self.title
