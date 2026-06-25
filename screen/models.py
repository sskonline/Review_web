from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

class Movie(models.Model):
    title = models.CharField(max_length=50)
    year =models.IntegerField()
    img_src= models.URLField()
    slug=models.SlugField(unique=True)

    def save(self ,*args, **kwargs):
        self.slug=slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
class Review(models.Model):
    title= models.ForeignKey(Movie, on_delete=models.CASCADE)
    user= models.ForeignKey(User , on_delete=models.CASCADE)
    review = models.TextField()
    created= models.DateTimeField(auto_now_add=True)