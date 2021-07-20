from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.files import ImageField
from django.http import Http404
from pyuploadcare.dj.models import ImageField

# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio=models.CharField(max_length=500,blank=True,default='No Bio')
    profile_pic=ImageField(blank=True,manual_crop="")
    contact=models.EmailField(max_length=30,blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save_profile(self):
        self.save()

class Project(models.Model):
    title=models.CharField(max_length=300)
    image=ImageField(manual_crop='')
    url=models.URLField(max_length=1000)
    description=models.TextField(max_length=1000)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='project')
    posted_on=models.DateField(auto_now_add=True)

    class Meta:
        ordering=['posted_on']

    def __str__(self):
        return self.title

    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()

    @classmethod
    def get_all_projects(cls):
        projects=cls.objects.order_by('-id')
        return projects


    


