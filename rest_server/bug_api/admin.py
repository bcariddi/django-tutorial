from django.contrib import admin

# Register your models here.
from .models import Bug, Comment

admin.site.register(Bug)
admin.site.register(Comment)
