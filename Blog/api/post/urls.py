from django.urls import path
from .views import *


urlpatterns = [
    path('posts/', PostListView.as_view()),
    path('posts/<int:pk>/', PostDetailView.as_view()),
    path('comments/', CommentView.as_view()),
    path('comments/<int:pk>', CommentDetailView.as_view()),
    path('tags/', TagsView.as_view()),
]
