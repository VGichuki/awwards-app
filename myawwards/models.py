from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.files import ImageField
from django.http import Http404
from pyuploadcare.dj.models import ImageField

# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, related_name='name')
    bio=models.CharField(max_length=500,blank=True,default='No Bio')
    profile_pic=ImageField(blank=True,manual_crop="")
    contact=models.CharField(max_length=30,blank=True)

    def __str__(self):
        return self.user.username

    def save_profile(self):
        self.save()

    


