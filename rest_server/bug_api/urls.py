from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:bug_id>/', views.BugView.as_view(), name='detail')   # ex: /bugs/5/
]