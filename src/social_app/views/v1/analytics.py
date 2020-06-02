from django.db.models import Count

from rest_framework.views import APIView
from rest_framework.response import Response

from social_app.models import Like
from .serializers.analytics import DateSerializer


class AnalyticView(APIView):

    def _validate_date(self):
        serializer = DateSerializer(data=self.request.query_params)
        serializer.is_valid(raise_exception=True)
        return serializer.data['date_from'], serializer.data['date_to']

    def _get_data(self):
        date_from, date_to = self._validate_date()
        data = Like.objects \
            .filter(date__range=(date_from, date_to)) \
            .values('date') \
            .annotate(total_likes=Count('id'))
        return data

    def get(self, request, *args, **kwargs):
        data = self._get_data()
        return Response(data)
