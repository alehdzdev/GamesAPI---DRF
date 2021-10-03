"""Games serializers."""
from rest_framework import serializers
from games.models import Platform, Developer, Genre, Publisher, Game


class PlatformSerializer(serializers.ModelSerializer):
    """Platform serializer."""
    class Meta:
        model = Platform
        fields = "__all__"


class DeveloperSerializer(serializers.ModelSerializer):
    """Developer serializer."""
    class Meta:
        model = Developer
        fields = "__all__"


class GenreSerializer(serializers.ModelSerializer):
    """Genre serializer."""
    class Meta:
        model = Genre
        fields = "__all__"


class PublisherSerializer(serializers.ModelSerializer):
    """Publisher serializer."""
    class Meta:
        model = Publisher
        fields = "__all__"


class GameSerializer(serializers.ModelSerializer):
    """Game serializer with the corresponded serializer as fields"""

    created_at = serializers.SerializerMethodField()
    developers = DeveloperSerializer(read_only=True)
    publishers = PublisherSerializer(read_only=True)
    genres = GenreSerializer(many=True, read_only=True)
    platforms = PlatformSerializer(many=True, read_only=True)

    class Meta:
        model = Game
        exclude = ["updated_at"]

    def get_created_at(self, instance):
        return instance.created_at.strftime("%B %d, %Y")
