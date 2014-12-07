from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='oser')
    picture = models.ImageField(upload_to='profile_images', blank=True)
    def __unicode__(self):
        return self.user

class Category(models.Model):
    title = models.CharField(max_length=65)
    slug = models.SlugField(unique=True)
    description = models.TextField(max_length=155)

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('view_blog_category', None , { 'slug': self.slug })


class Post(models.Model):
    author = models.ForeignKey(User)
    categories = models.ManyToManyField(Category)
    title = models.CharField(max_length=65)
    slug = models.SlugField(unique=True)
    description = models.TextField(max_length=155)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        ordering = ['-timestamp',]\

    def __unicode__(self):
        return self.title

    def get_previous_post(self):
        return self.get_previous_by_timestamp()

    def get_next_post(self):
        return self.get_next_by_timestamp()

    @models.permalink
    def get_absolute_url(self):
        return ('view_blog_post', None , {'slug': self.slug})

