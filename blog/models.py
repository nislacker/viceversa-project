from django.db import models

# Create your models here.
class Post(models.Model):

    title = models.CharField(max_length=300)
    text = models.TextField()
    date = models.DateTimeField()
    image = models.ImageField(upload_to='event_images/')