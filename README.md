# Python Backend Developer Test

## Overview:

This repo containts a Django project as evaluation for a Python Backend Developer position. The description of the project can be found in this link: 

## How to run the project:

1. TODO
2. TODO
3. TODO
4. TODO

## Code structure overview:

The project folder contains a folder with top_songs app that contains three models, a viewset and some serializers. The root folder contains the file requirements.txt for installing dependencies.

## Solution description

Because we have to create an API for exposing top music data, the first thing to do is download JSON file and explore it with a JSON viewer app to see data schema.
The JSON have, besides some general info describing the content of the file, a list of record with each record having the following info:

            {
                "artistName": "Taylor Swift",
                "id": "1650841515",
                "name": "Anti-Hero",
                "releaseDate": "2022-10-21",
                "kind": "songs",
                "artistId": "159260351",
                "artistUrl": "https://music.apple.com/us/artist/taylor-swift/159260351",
                "artworkUrl100": "https://is4-ssl.mzstatic.com/image/thumb/Music122/v4/59/13/5c/59135ccc-8425-415c-7f89-8aeada60088e/22UM1IM22440.rgb.jpg/100x100bb.jpg",
                "genres": [
                    {
                        "genreId": "14",
                        "name": "Pop",
                        "url": "https://itunes.apple.com/us/genre/id14"
                    },
                    {
                        "genreId": "34",
                        "name": "Music",
                        "url": "https://itunes.apple.com/us/genre/id34"
                    }
                ],
                "url": "https://music.apple.com/us/album/anti-hero/1650841512?i=1650841515"
            }


According to this, we could have a data schema with the following entities:
. Artist
. Genre
. Track

For the solution of the given exercise we will have to go againts the requirements of having four endpoints. We will follow best practices in API design (https://swagger.io/resources/articles/best-practices-in-api-design/) and those four endpoints refers to one unique resource: tracks. So we will have this endpoint only: /api/v0/tracks. Having that unique endpoint, each of the exercises will resolved as follows:

1. An endpoint to provide a search lookup within the tracks: GET /api/v0/tracks?name='Rihanna'
2. An endpoint that would allow to get the top 50 popularity tracks: GET /api/v0/tracks?limit=10
3. An endpoint to remove a track, using a given identifier: DELETE /api/v0/tracks/1650841515
4. An endpoint to add new tracks using ORM: POST /api/v0/tracks

Note that we are using HTTP methods to define the CRUD operations for any track resource or tracks resources collection.

Due to we use Test Driven Development, we taked each exercise as a user history and started a process of test and error until each user history (exercise) be completed.

We created a django project and named it music_track. Then we added a new application named top_songs.

Our first test case was to get a list of tracks. When we run "python manage.py test", we first got error importing the Track model, so we had to create it with the other two models and their relations, make the migrations and migrate.

Then we get a 404 error. That is because we have to create an URL conf. We create de URLS using django rest framework (DRF) SimpleRouter. From routing we will use DRF ModelViewSet for handling all HTTP methods associated to track resource in a single class, and finally we created a serializer class for Track model.

Once we have the endpoint for getting the track list working, we need to add data to database. For this we use a migration. This migration will read the json file and will fill tables with data. The migration is runned when calling the migrate command.

Once we have the endpoint returning all records we can then add filter options. We can do this in easy way with SearchFilter from DRF in the ViewSet. We defined search fields for track name and artist name.

For limiting the amount of records we set  





