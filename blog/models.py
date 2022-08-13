from django.contrib.auth.models import User
from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    date = models.DateField(auto_now=True)
    thumb = models.ImageField(default='image.jpg', blank=True)
    author = models.ForeignKey(User, default=None, null=True,  on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='article_likes')
    dislikes = models.ManyToManyField(User, related_name='article_dislikes')

    
    def __str__(self):
        return self.title

    def snippet(self):
        return self.text[:20] + '... read more'

    def total_likes(self):
        return self.likes.count()

    def total_dislikes(self):
        return self.dislikes.count()    
            
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.article} - {self.body[:5]}'
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    followers = models.ManyToManyField(User, related_name="followers", blank=True)
    followings = models.ManyToManyField(User, related_name="followings", blank=True)
    profile_picture = models.ImageField(default='profile_picture.jpg', null=True) 
    favorites = models.ManyToManyField(Article)
        
    def __str__(self):
        return self.user.username