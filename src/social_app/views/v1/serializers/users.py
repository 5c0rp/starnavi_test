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
        return instance.last_login.strftime('%Y-%m-%dT%H:%M:%S')

    def get_last_activity(self, instance):
        return instance.last_activity.strftime('%Y-%m-%dT%H:%M:%S')

    def create(self, validated_data):
        user = User(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
