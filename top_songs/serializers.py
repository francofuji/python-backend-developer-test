from rest_framework.serializers import ModelSerializer

from top_songs.models import Track, Artist, Genre


class GenreSerializer(ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class ArtistSerializer(ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'

class TrackSerializer(ModelSerializer):
    artist = ArtistSerializer()
    class Meta:
        model = Track
        fields = '__all__'

    
    def create(self, validated_data):
        artist_data = validated_data.pop('artist')
        artist, created = Artist.objects.get_or_create(artistUrl=artist_data['artistUrl'], defaults={
            'artistName': artist_data['artistName']
        })
        genres = validated_data.pop('genres')
        track_instance = Track.objects.create(artist=artist, **validated_data)
        track_instance.artist = artist
        track_instance.save()
        for genre_data in genres:
            track_instance.genres.add(genre_data)

        return track_instance