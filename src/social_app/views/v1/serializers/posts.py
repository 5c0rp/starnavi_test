from rest_framework import serializers

from social_app import services as likes_services
from social_app.models import Post


class PostSerializer(serializers.ModelSerializer):
    is_fan = serializers.SerializerMethodField()
    author = serializers.SerializerMethodField()
    pub_date = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = (
            'id',
            'author',
            'subject',
            'body',
            'pub_date',
            'total_likes',
            'is_fan',
        )
        read_only_fields = (
            'pub_date',
            'total_likes',
            'is_fan'
        )

    def get_author(self, instance):
        return instance.author.username

    def get_is_fan(self, instance):
        user = self.context.get('request').user
        return likes_services.is_fan(instance, user)

    def get_pub_date(self, instance):
        return instance.pub_date.strftime('%Y-%m-%dT%H:%M:%S')

    def create(self, validated_data):
        user = self.context.get('request').user
        instance = Post.objects.create(author=user, **validated_data)
        return instance
