from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser 
from django.shortcuts import reverse

# Create your models here.
class User_model(AbstractUser):
    #REQUIRED_FIELDS = ('user',)
    #USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username

class Post(models.Model):

    title = models.CharField(max_length=100)
    content = models.TextField()
    thumbnail = models.ImageField()
    publish_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User_model , on_delete = models.CASCADE)
    slug = models.SlugField()
    
    def __str__(self):
        return self.title
    
    def post_edit(self):
        
        return reverse("update", kwargs={
            'slug' : self.slug
        })    

    def get_absolute_url(self):
        return reverse("detail", kwargs={
            'slug' : self.slug
        })
    
    def get_like_url(self):
        return reverse("like", kwargs={
            'slug' : self.slug
        })

    def get_update_url(self):
        return reverse("update", kwargs={
            'slug' : self.slug
        })
    
    def get_delete_url(self):
        return reverse("delete", kwargs={
            'slug' : self.slug
        })
    
    @property
    def comments(self):
        return self.comment_set.all()

    @property
    def get_comment_count(self):
        return self.comment_set.all().count()

    @property
    def get_view_count(self):
        return self.postview_set.all().count()

    @property
    def get_like_count(self):
        return self.like_set.all().count()

class Comment(models.Model):

    user = models.ForeignKey(User_model , on_delete = models.CASCADE)
    post = models.ForeignKey(Post , on_delete= models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class PostView(models.Model):

    user = models.ForeignKey(User_model , on_delete = models.CASCADE)
    post = models.ForeignKey(Post , on_delete= models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class Like(models.Model):

    user = models.ForeignKey(User_model , on_delete = models.CASCADE)
    post = models.ForeignKey(Post , on_delete= models.CASCADE)

    def __str__(self):
        return self.user.username

        