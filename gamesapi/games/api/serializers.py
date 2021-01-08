from rest_framework import serializers
from games.models import Platform, Developer, Genre, Publisher, Game


class PlatformSerializer(serializers.ModelSerializer):

    class Meta:
        model = Platform
        fields = "__all__"


class DeveloperSerializer(serializers.ModelSerializer):

    class Meta:
        model = Developer
        fields = "__all__"


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = "__all__"


class PublisherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Publisher
        fields = "__all__"


class GameSerializer(serializers.ModelSerializer):

    created_at = serializers.SerializerMethodField()
    developers = DeveloperSerializer(many=True, read_only=True)
    publishers = PublisherSerializer(many=True, read_only=True)
    genres = GenreSerializer(many=True, read_only=True)
    platforms = PlatformSerializer(many=True, read_only=True)

    class Meta:
        model = Game
        exclude = ["updated_at"]

    def get_created_at(self, instance):
        return instance.created_at.strftime("%B %d, %Y")