from django.db import models

# Create your models here.
class Subscriber(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email()

class Category(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

class Project(models.Model):
    title = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    description = models.TextField()
    categories = models.ManyToManyField('Category')
    imageURL = models.URLField(default='')
    imgCaption = models.CharField(max_length=100) # place in small text under the image
    #thumbnail = models.FilePathField(path="/img") # Or: imageURL = models.URLField(default='')

    def __str__(self):
        return self.title

    


