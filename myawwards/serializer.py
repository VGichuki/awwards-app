from rest_framework import serializers
from .models import Project,Profile
from django.contrib.auth.models import User

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['profile_pic', 'bio', 'contact', 'user']

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['user', 'title', 'image', 'description', 'url', 'posted_on']

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only = True)
    project = ProjectSerializer(many=True, read_only = True)
    class Meta:
        model = User
        fields = ['user', 'url', 'username', 'profile', 'projects']
