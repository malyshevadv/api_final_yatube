from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from rest_framework import filters, permissions, status, viewsets
from rest_framework.pagination import LimitOffsetPagination

from posts.models import Group, Post

from .permissions import IsAuthorOrReadOnly
from .serializers import (CommentSerializer, FollowerSerializer,
                          GroupSerializer, PostSerializer)
from .viewsets import CreateRetrieveViewSet


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsAuthorOrReadOnly
    )
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsAuthorOrReadOnly
    )

    def get_queryset(self):
        post_id = self.kwargs.get("post_id")
        post = get_object_or_404(Post, pk=post_id)
        comments_list = post.comments.all()
        return comments_list

    def perform_create(self, serializer):
        post_id = self.kwargs.get("post_id")
        post = get_object_or_404(Post, pk=post_id)
        serializer.save(post=post, author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (permissions.AllowAny,)


class FollowViewSet(CreateRetrieveViewSet):
    serializer_class = FollowerSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.SearchFilter, )
    search_fields = ('^following__username',)

    def get_queryset(self):
        return self.request.user.follower.all()

    def perform_create(self, serializer):
        user = self.request.user
        if user.username == self.request.data["following"]:
            raise ValidationError(
                'Вы не можете подписаться сами на себя.',
                status.HTTP_400_BAD_REQUEST
            )
        try:
            serializer.save(user=self.request.user)
        except IntegrityError:
            raise ValidationError(
                'Вы уже подписаны на этого автора.',
                status.HTTP_400_BAD_REQUEST
            )
