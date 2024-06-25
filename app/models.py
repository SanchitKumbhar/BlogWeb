from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class userdetails(models.Model):
    name = models.CharField(max_length=150)
    phonenumber = models.CharField(max_length=150)
    college = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    hobbies=models.CharField(max_length=150,blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

class ip(models.Model):
    ipadd=models.CharField(max_length=128)
    blogid=models.CharField(max_length=128)
    def __str__(self):
        return self.ipadd

class likeip(models.Model):
    likedip=models.CharField(max_length=128)
    blogid=models.CharField(max_length=128)


class Blog(models.Model):
    blogtitle=models.CharField(max_length=150)
    blogcontent=models.TextField(max_length=2000)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    views=models.ManyToManyField(ip)
    ipliked=models.ManyToManyField(likeip)
    userliked = models.ManyToManyField(User,related_name="userliked")


    def total_views(self):
        return self.views.count()
    def total_likes(self):
        return self.ipliked.count()
    
class comments(models.Model):
    comment=models.CharField(max_length=3000)
    blogid=models.CharField(max_length=128)
    usercomment = models.ForeignKey(User,related_name="usercomment",on_delete=models.CASCADE)


class Search(models.Model):
    search=models.CharField(max_length=150)
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True)







