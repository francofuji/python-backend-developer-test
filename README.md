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



