import json
import requests
from secrets import spotify_user_id, playlist_id
from refresh import Refresh

class SaveSongs:
    def __init__(self):
        self.user_id = spotify_user_id
        self.user_token = Refresh().newToken
        self.playlist_id = playlist_id
        self.tracks =''

    def find_songs(self):
        #get songs in playlits
        print('Retrieving Songs....')
        query = 'https://api.spotify.com/v1/playlists/{}/tracks'.format(playlist_id)

        response = requests.get(query, 
                                headers = {'content-Type':'application/json',
                                            'Authorization':'Bearer {}'.format(self.user_token)}
                                )
        response_json = response.json()
        print(response_json.keys())
        for i in response_json['items']:
            self.tracks+=(i['track']['name']+',')
     

        #self.tracks=self.tracks[:-1]

a = SaveSongs()
a.find_songs()
print(a.tracks)
