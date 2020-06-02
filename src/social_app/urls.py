from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('v1/', include('social_app.views.v1.urls'))
]
