from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'bugs', views.BugViewSet)
router.register(r'comments', views.CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('bugs/', views.BugIndexView.as_view(), name='index'),
    path('bugs/<int:pk>/', views.BugView.as_view(), name='detail'),   # ex: /bugs/5/
    path('comments/', views.CommentIndexView.as_view(), name='index'),
    path('comments/<int:pk>/', views.CommentView.as_view(), name='detail')
]