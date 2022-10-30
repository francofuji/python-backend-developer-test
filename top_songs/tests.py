from rest_framework.test import APITestCase

from top_songs.models import Track

class TrackAPITestCase(APITestCase):

    def test_list_tracks(self):
        """
        Test that we can get a list of tracks
        """
        response = self.client.get('/api/v0/tracks/')
        self.assertEqual(response.status_code, 200)
