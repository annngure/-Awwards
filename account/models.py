from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# # Create your models here.

class Image(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE,null=True)
    image = CloudinaryField('image')
    name = models.CharField(max_length=60)
    likes= models.IntegerField(default=0)
    caption = models.TextField()
  

    def save_image(self):
        self.save()
    
    @classmethod
    def display_image(cls):
        images=cls.objects.all()
        return images

    @classmethod
    def search_image(cls,search_term):
        images = cls.object.filter(name_icontains = search_term).all()
        return images

    def delete_image(self):
        self.delete()

    def __str__(self):
        return self.name
   

class Profile(models.Model):
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length =30, null=True)
    profile_image = models.ImageField(upload_to='image')
    bio = models.TextField(blank = True)
    username = models.CharField(default='user',max_length=30)

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def __str__(self):
        return self.last_name

    @classmethod
    def search_profile(cls,search_term):
        profile =cls.objects.filter(first_name_icontains =search_term)

class Comment(models.Model):
    comment = models.TextField(blank= True,null=True)
    image = models.ForeignKey(Image,on_delete = models.CASCADE,null=True)
    user = models.ForeignKey(User,on_delete = models.CASCADE)

    def delete_comment(self):
        self.delete()

    def save_comment(self):
        self.save()

    def __str__(self):
        return self.comment

        
class Follows(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE,related_name='follow',null=True)
    follower = models.ForeignKey(Profile,on_delete = models.CASCADE, null = True)

    def save_follower(self):
        self.save

    def delete_follower(self):
        self.save

    def __int__(self):
        return self.name