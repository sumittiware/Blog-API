from django.shortcuts import render
from rest_framework import generics,permissions
from .models import *
from .serializers import *
from .pagination import *
from .permissions import *

# VIEWS

# Post Views
# Postes can only be viewed at /posts/
class PostListView(generics.ListAPIView):
    serializer_class = PostListSerializer
    pagination_class = PostPaginatonClass

    def get_queryset(self):
        query = self.request.query_params

        #TODO: add postgre sql database to _icontains to work
        if 'search' in query:
            posts = Post.objects.order_by('-created_at').filter(title=query['search'])
            return posts

        posts = Post.objects.order_by('-created_at')
        
        if 'author' in query:
            posts = posts.filter(author=query['author'])
        if 'tag' in query:
            posts = posts.filter(tags=query['tag'])

        return posts

class PostDetailView(generics.RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    permission_class = (permissions.IsAuthenticated,isAuthorOrReadOnly,)
    serializer_class = PostDetailSerializer


# Comment Views
# the comment can only be created at /comments/
class CommentView(generics.ListCreateAPIView):
    queryset=Comment.objects.all()
    permission_class = (permissions.IsAuthenticated,)
    serializer_class = CommentSerializer

# only authenticated user and the who has written the comment can delete or update the comment at /comments/:id
class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Comment.objects.all()
    permission_class = (permissions.IsAuthenticated,isCommentorOrReadOnly)
    serializer_class = CommentSerializer


# Tags Views
# it's a list view so that is cannot be updated by user in any case at /tags/
class TagsView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagsDetail


