from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Tag,Post,Comment

# SERIALIZERS

class UserSerializer(serializers.ModelSerializer): 
    class Meta:
        model = get_user_model()
        fields = ('id', 'username','email',)

# TAGS SERIALIZERS
# this is used to return the many many to field as list 
class TagsListingField(serializers.RelatedField):
    def to_representation(self, value):
        return value.name


class TagsDetail(serializers.ModelSerializer):
    class Meta:
        model=Tag
        fields=(
            'id',
            'name',
            'created_at',
        )

# COMMENT SERIALIZERS
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields=(
            'id',
            'user',
            'post',
            'content',
            'created_at',
        )


# POST SERIALIZERS
class PostListSerializer(serializers.HyperlinkedModelSerializer):
    tags = TagsListingField(read_only=True,many=True)
    author = UserSerializer()
    class Meta:
        model=Post
        fields=(
            'id',
            'title',
            'author',
            'tags',
            'created_at',
        )

class PostDetailSerializer(serializers.HyperlinkedModelSerializer):
    tags = TagsListingField(read_only=True,many=True)
    author = UserSerializer()
    class Meta:
        model=Post
        fields=(
            'id',
            'title',
            'body',
            'author',
            'tags',
            'created_at',
            'updated_at',
        )