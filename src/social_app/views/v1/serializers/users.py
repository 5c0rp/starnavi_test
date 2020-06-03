from django.contrib.auth import get_user_model

from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    last_login = serializers.SerializerMethodField()
    last_activity = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            'username',
            'password',
            'last_login',
            'last_activity',
        )
        extra_kwargs = {
            'password': {'write_only': True}
        }
        read_only_fields = (
            'last_login',
            'last_activity',
        )

    def get_last_login(self, instance):
        time = instance.last_login
        return time.strftime('%Y-%m-%dT%H:%M:%S') if time else None

    def get_last_activity(self, instance):
        time = instance.last_activity
        return time.strftime('%Y-%m-%dT%H:%M:%S') if time else None

    def create(self, validated_data):
        user = User(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
