from django.db import models

class ImageModel(models.Model):
    original_image = models.ImageField(upload_to='original_images/')
    bw_image = models.ImageField(upload_to='bw_images/', blank=True, null=True)

    def __str__(self):
        return f"Image {self.id}"
