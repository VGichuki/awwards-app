from rest_framework import serializers
from .models import Project,Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['profile_pic', 'bio', 'contact', 'user']

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['user', 'title', 'image', 'description', 'url', 'posted_on']

