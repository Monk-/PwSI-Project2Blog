from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='oser')
    picture = models.ImageField(blank=True)

    def __unicode__(self):
        return self.user

    @models.permalink
    def get_absolute_url(self):
        return ('view_profile_author', None , { 'author': self.user })


class Category(models.Model):
    title = models.CharField(max_length=65)
    slug = models.SlugField(unique=True)
    description = models.TextField(max_length=155)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    def save(self):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Category, self).save()

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
        ordering = ['-timestamp', ]

    def __unicode__(self):
        return self.title

    def save(self):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save()

    @models.permalink
    def get_absolute_url(self):
        return ('view_blog_post', None, {'slug': self.slug})


class Comments(models.Model):
    body = models.TextField()
    author = models.ForeignKey(User, related_name= 'upser')
    timestamp = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(Post, related_name='comments')

    class Meta:
        ordering = ('-timestamp',)