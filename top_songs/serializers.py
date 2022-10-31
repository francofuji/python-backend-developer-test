from rest_framework.serializers import ModelSerializer

from top_songs.models import Track

class TrackSerializer(ModelSerializer):
    class Meta:
        model = Track
        fields = '__all__'