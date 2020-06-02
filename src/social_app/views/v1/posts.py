from rest_framework.routers import SimpleRouter
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from social_app.models import Post
from social_app.mixins import LikedMixin
from social_app.permissions import IsOwnerOrReadOnly

from .serializers.posts import PostSerializer


class PostViewSet(LikedMixin, ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_permissions(self):
        if self.action in ('update', 'partial_update', 'destroy'):
            self.permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
        return super().get_permissions()


router = SimpleRouter()
router.register('posts', PostViewSet)
