from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin

from .serializers.users import UserSerializer


class SignUpView(CreateModelMixin, GenericAPIView):
    authentication_classes = ()
    permission_classes = ()

    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
