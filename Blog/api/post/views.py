from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import generics,permissions
from django.views.decorators.vary import vary_on_cookie, vary_on_headers

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
        posts = Post.objects.order_by('-created_at')

        #TODO: add postgre sql database to _icontains to work
        if 'search' in query:
            posts = posts.filter(title=query['search'])
            return posts
        
        if 'author' in query:
            posts = posts.filter(author=query['author'])
        if 'tag' in query:
            posts = posts.filter(tags=query['tag'])

        return posts

class PostDetailView(generics.RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    permission_class = (permissions.IsAuthenticated,isAuthorOrReadOnly,)
    serializer_class = PostDetailSerializer

    # With auth: cache requested url for each user for 2 hours
    @method_decorator(cache_page(60*60*2))
    @method_decorator(vary_on_headers("Authorization",))
    def get_queryset(self):
        return Post.objects.all()


# Comment Views
# the comment can only be created at /comments/
class CommentView(generics.ListCreateAPIView):
    permission_class = (permissions.IsAuthenticated,)
    serializer_class = CommentSerializer

    # With auth: cache requested url for each user for 2 hours
    @method_decorator(cache_page(60*60*2))
    @method_decorator(vary_on_headers("Authorization",))
    def get_queryset(self):
        query = self.request.query_params
        comments = Comment.objects.order_by('-created_at').filter(post=query['postId'])
        return comments


# only authenticated user and the who has written the comment can delete or update the comment at /comments/:postId
class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Comment.objects.all()
    permission_class = (permissions.IsAuthenticated,isCommentorOrReadOnly)
    serializer_class = CommentSerializer

    
# Tags Views
# it's a list view so that is cannot be updated by user in any case at /tags/
class TagsView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagsDetail


