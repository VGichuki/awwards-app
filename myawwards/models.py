from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.files import ImageField
from django.http import Http404
from pyuploadcare.dj.models import ImageField
import datetime as dt
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio=models.CharField(max_length=500,blank=True,default='No Bio')
    profile_pic=models.ImageField(blank=True,upload_to='images/', default='')
    contact=models.EmailField(max_length=30,blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save_profile(self):
        self.save()


class Project(models.Model):
    title=models.CharField(max_length=300)
    image=models.ImageField(upload_to='projects/')
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

class Rating(models.Model):
    rating = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
    )
    design = models.IntegerField(choices=rating, default=0, blank=True)
    usability = models.IntegerField(choices=rating, blank=True)
    content = models.IntegerField(choices=rating, blank=True)
    score = models.FloatField(default=0, blank=True)
    design_average = models.FloatField(default=0, blank=True)
    usability_average = models.FloatField(default=0, blank=True)
    content_average = models.FloatField(default=0, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='rater')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='ratings', null=True)

    def save_rating(self):
        self.save()

    @classmethod
    def get_ratings(cls, id):
        ratings = Rating.objects.filter(post_id=id).all()
        return ratings

        def __str__(self):
            return f'{self.project}Rating'

    


