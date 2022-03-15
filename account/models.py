from django.db import models
from django.contrib.auth.models import User
# from cloudinary.models import CloudinaryField


# # Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=50)
    

    def save_location(self):
        self.save

    def delete_location(self):
        self.delete

    def __int__(self):
        return self.name

class Project(models.Model):
    title= models.TextField(max_length=200, null=True )
    project_image =models.ImageField(upload_to='image', blank = True)
    description = models.TextField()
    project_url = models.URLField(max_length=250, blank=True)
  

    def save_project(self):
        self.save()


    def delete_project(self):
        self.delete()


    def __str__(self):
        return self.name
   

class Profile(models.Model):
    user= models.OneToOneField(User, null = True , related_name ='profile',on_delete = models.CASCADE)
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length =30, null=True)
    profile_image = models.ImageField(upload_to='image', blank = True)
    bio = models.TextField(blank = True)
    project =models.ForeignKey(Project, null = True,on_delete=models.CASCADE)

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def __str__(self):
        return self.last_name

    @classmethod
    def search_profile(cls,search_term):
        profile =cls.objects.filter(first_name_icontains =search_term)




class Image(models.Model):
    image = models.ImageField(upload_to='image', blank = True)
    name=models.CharField(max_length=40)
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    description=models.CharField(max_length=2000)
    location=models.ForeignKey(Location,null=True,on_delete = models.CASCADE)
    likes = models.IntegerField(default=0)
    comment = models.TextField(blank= True)
   

    def delete_image(self):
        self.delete()

    def save_image(self):
        self.save()

    def __str__(self):
        return self.name

        
