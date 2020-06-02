from rest_framework_jwt.views import obtain_jwt_token
from django.urls import path, include

from .analytics import AnalyticView
from .signup import SignUpView
from . import posts
from . import users

urlpatterns = [
    path('login', obtain_jwt_token),
    path('signup', SignUpView.as_view()),
    path('analytics', AnalyticView.as_view()),

    path('', include(users.router.urls)),
    path('', include(posts.router.urls)),

]
