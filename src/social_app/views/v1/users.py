from rest_framework.routers import SimpleRouter
from rest_framework.viewsets import ReadOnlyModelViewSet

from .serializers.users import UserSerializer, User


class UserViewSet(ReadOnlyModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


router = SimpleRouter()
router.register('users', UserViewSet)
