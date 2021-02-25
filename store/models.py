from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager


class Picture(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date_uploaded = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to="pictures")
    tags = TaggableManager()

    def __str__(self):
        return self.name
