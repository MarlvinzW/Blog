from django.db import models
from PIL import Image
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    picture = models.ImageField(default='default.png', upload_to='profiles')

    class Meta:
        verbose_name_plural = 'Users'
        ordering = ['username']

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.picture:
            img = Image.open(self.picture.path)
            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.picture.path)


