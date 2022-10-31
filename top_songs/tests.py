from django.test import TestCase

from rest_framework.test import APITestCase

from top_songs.models import Track

class TrackAPITestCase(APITestCase):

    def test_list_tracks(self):
        """
        Test that we can get a list of tracks
        """
        response = self.client.get('/api/v0/tracks/')
        self.assertEqual(response.status_code, 200)

class TrackDBTestCase(TestCase):

    def test_db_have_data(self):
        """
        Test that database have some data
        """
        self.assertEqual(True, Track.objects.count() > 0)