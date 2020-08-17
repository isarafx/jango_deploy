from django.db import models


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=80)
    age = models.IntegerField()
    job = models.CharField(max_length=40)
    profile_pic = models.ImageField(upload_to="profile_images")

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    featured_image = models.ImageField(upload_to="featured_photos")
    reporter = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


