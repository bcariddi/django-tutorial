from rest_framework import serializers

from .models import Bug, Comment

class BugSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bug
        fields = ['package', 'status', 'version', 'summary']

class CommentSerializer(serializers.ModelSerializer):
    bug = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Comment
        fields = ['bug', 'user', 'content']
