from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from rest_framework import viewsets, permissions

from .serializers import BugSerializer, CommentSerializer
from .models import Bug, Comment

class BugIndexView(generic.ListView):
    template_name = 'bug_api/bug_index.html'
    context_object_name = 'bug_list'

    def get_queryset(self):
        return Bug.objects.order_by('-id')

class BugView(generic.DetailView):
    model = Bug
    template_name = 'bug_api/bug.html'

class CommentIndexView(generic.ListView):
    template_name = 'bug_api/comment_index.html'
    context_object_name = 'comment_list'

    def get_queryset(self):
        return Comment.objects.order_by('-id')

class CommentView(generic.DetailView):
    model = Comment
    template_name = 'bug_api/comment.html'

class BugViewSet(viewsets.ModelViewSet):
    queryset = Bug.objects.all().order_by('-id')
    serializer_class = BugSerializer
    permission_classes = [permissions.IsAuthenticated]

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]