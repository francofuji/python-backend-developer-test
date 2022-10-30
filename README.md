# Python Backend Developer Test

## Overview:

This repo containts a Django project as evaluation for a Python Backend Developer position. The description of the project can be found in this link: 

## How to run the project:

1. TODO
2. TODO
3. TODO
4. TODO

## Code structure overview:


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


