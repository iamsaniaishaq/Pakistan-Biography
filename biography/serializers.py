# serializers.py
from rest_framework import serializers
from django.conf import settings
from .models import PrimeMinisters

class PrimeMinistersSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = PrimeMinisters
        fields = [
            'id',
            'name',
            'english_bio',
            'urdu_bio',
            'english_achievements',
            'urdu_achievements',
            'youtube_link',
            'background_color',
            'term',
            'image_url',  # Include the image_url in the response
        ]

    def get_image_url(self, obj):
        if obj.image:
            return f"http://127.0.0.1:8000/media/{obj.image.name}"  # Return full URL to the image
        return None  # Return None if no image is available
