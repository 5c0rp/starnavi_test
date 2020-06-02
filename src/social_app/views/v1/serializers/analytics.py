from rest_framework import serializers


class DateSerializer(serializers.Serializer):
    date_from = serializers.DateField()
    date_to = serializers.DateField()

    def validate(self, attrs):
        if attrs['date_from'] > attrs['date_to']:
            raise serializers.ValidationError(
                {'date_from': 'can\'t be greater than date_to'}
            )

        return attrs
