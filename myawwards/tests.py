from django.contrib.auth.models import User
from django.test import TestCase
from .models import Profile, Project,Rating, User

# Create your tests here.
class ProfileTestClass(TestCase):
    def setUp(self):
       self.user = User(username='wangari', password='Nyeri12032!',email='vivian.gichuki@student.moringaschool.com')
       self.user.save()

       self.profile =Profile(user=self.user, bio='Software developer', profile_pic='', contact='vivian.gichuki@student.moringaschool.com')


    def test_instance(self):
        self.assertTrue(isinstance(self.profile, Profile))

    def test_save_profile(self):
        self.profile.save()

class ProjectTestClass(TestCase):
       

    

