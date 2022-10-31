# Generated by Django 4.1.2 on 2022-10-31 05:01
from email.policy import default
import json
import datetime
from django.db import migrations

def fill_database(apps, schema_editor):
    """
    Read songs.json file and fill database
    """
    Track = apps.get_model('top_songs', 'Track')
    Artist = apps.get_model('top_songs', 'Artist')
    Genre = apps.get_model('top_songs', 'Genre')
    
    f = open('./songs.json')
    data = json.load(f)
    for json_track in data['feed']['results']:
        try:
            artist = Artist.objects.get(id=int(json_track['artistId']))
        except:
            artist = Artist()
            artist.id = int(json_track['artistId'])
        artist.artistName = json_track['artistName']
        artist.artistUrl = json_track['artistUrl']
        artist.save()
        """
        track, created = Track.objects.get_or_create(id=int(json_track['id']), defaults={
            'releaseDate': datetime.datetime.strptime(json_track['releaseDate'], '%Y-%m-%d'),
            'artist': artist,
            'name': json_track['name'],
            'artworkUrl100': json_track['artworkUrl100'],
            'url': json_track['url'],
        })
        if created:
            if 'contentAdvisoryRating' in json_track:
                track.contentAdvisoryRating = json_track['contentAdvisoryRating']
                track.save()
        for json_genre in json_track['genres']:
            genre, created = Genre.objects.get_or_create(id=int(json_genre['genreId']), defaults={
                'name': json_genre['name'],
                'url': json_genre['url']
            })
            track.genres.add(genre)
        """
    
    f.close()

def reverse(apps, schema_editor):
    """
    Clear database
    """
    Track = apps.get_model('top_songs', 'Track')
    Artist = apps.get_model('top_songs', 'Artist')
    Genre = apps.get_model('top_songs', 'Genre')
    Track.objects.all().delete()
    Artist.objects.all().delete()
    Genre.objects.all().delete()

class Migration(migrations.Migration):
    """
    Migration for fill database with info in songs.json file
    """

    dependencies = [
        ('top_songs', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(fill_database, reverse),
    ]