from django.db import models

# Create your models here.
#02
class Group(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title




class Post(models.Model):
    title = models.CharField(max_length = 200, blank = True) #01
    text = models.TextField()
    #group = models.ForeignKey(Group, on_delete=models.SET_NULL, blank = True, null = True, related_name = "post_group")
    comment = models.TextField()

    def __str__(self):
        return self.text
