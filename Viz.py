import json
import requests
from secrets import spotify_user_id, playlist_id
from refresh import Refresh

class SaveSongs:
    def __init__(self):
        self.user_id = spotify_user_id
        self.user_token = Refresh().newToken
        self.playlist_id = playlist_id
        self.tracks_uri =''
        self.tracks_name = ''
        self.num_tracks = 0
        self.track_dict = {}

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
        self.num_tracks = len(response_json['items'])
        for i in response_json['items']:
            self.tracks_uri+=(i['track']['uri']+',').split(':')[-1]
            self.tracks_name+=(i['track']['name']+',').split(':')[-1]
        self.tracks_uri = self.tracks_uri.split(',')
        self.tracks_name = self.tracks_name.split(',')
        self.track_dict = {self.tracks_name[i]: [self.tracks_uri[i]] for i in range(self.num_tracks)}
        return
        #self.tracks=self.tracks[:-1]

    def get_song_features(self):
        self.find_songs()
        print('Taking audio features')
        for track in self.track_dict.keys():
            song = self.track_dict[track][0]
            query = 'https://api.spotify.com/v1/audio-features/{}'.format(song)
            response = requests.get(query, 
                                headers = {'content-Type':'application/json',
                                            'Authorization':'Bearer {}'.format(self.user_token)
                                            }
                               )
            self.track_dict[track].append(response.json())
            #print(response.json(),'-'*30)
        return

a = SaveSongs()
#a.find_songs()
a.get_song_features()
info = a.track_dict
print(info['Succession (Main Title Theme) - Extended Intro Version'])
