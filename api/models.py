from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.


class Campaign(models.Model):

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=300)
    description = models.TextField()
    logo = CloudinaryField("Image", overwrite=True, format="jpg")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ('-created_at', )


class Subscriber(models.Model):

    email = models.EmailField()
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.email

    class Meta:
        ordering = ('-created_at', )
