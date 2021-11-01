from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Bug, Comment

class IndexView(generic.ListView):
    template_name = 'bug_api/index.html'
    context_object_name = 'latest_bug_list'

    def get_queryset(self):
        """Return the last five bugs."""
        return Bug.objects.order_by('-id')[:5]

class BugView(generic.DetailView):
    model = Bug
    template_name = 'bug_api/bug.html'