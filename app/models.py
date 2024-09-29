from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# profile deatils
class userdetails(models.Model):
    name = models.CharField(max_length=150)
    phonenumber = models.CharField(max_length=150)
    college = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    hobbies=models.CharField(max_length=150,blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    followers=models.ManyToManyField(User,related_name="followers")    

# ip address for views
class viewsip(models.Model):
    ipadd=models.CharField(max_length=128)
    blogid=models.CharField(max_length=128)
    def __str__(self):
        return self.ipadd



class Blog(models.Model):
    blogtitle=models.CharField(max_length=150)
    blogcontent=models.TextField(max_length=2000)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    views=models.ManyToManyField(User,related_name="views")
    userliked = models.ManyToManyField(User,related_name="userliked")       
    tagged_user=models.ManyToManyField(userdetails)


    def total_views(self):
        return self.views.count()
    def total_likes(self):
        return self.userliked.count()

            # def total_blogs(self):
            #     return self.blogtitle.count()
    
class comments(models.Model):
    comment=models.CharField(max_length=3000)
    blogid=models.CharField(max_length=128)
    usercomment = models.ForeignKey(User,related_name="usercomment",on_delete=models.CASCADE)


class Search(models.Model):
    search=models.CharField(max_length=150)
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True)
