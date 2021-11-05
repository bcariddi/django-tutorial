from rest_framework import serializers

from .models import Bug, Comment

class BugSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bug
        fields = ['package', 'status', 'version', 'summary']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['bug', 'user', 'content']
