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
        self.track_analysis = {}

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
        return True 
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

            nextRequest = requests.get('https://api.spotify.com/v1/audio-analysis/{}'.format(song),
                                    headers = {'content-Type':'application/json',
                                            'Authorization':'Bearer {}'.format(self.user_token)
                                            }
                                )
            currA = nextRequest.json()
            self.track_analysis[track]=[song,currA['sections'],currA['segments']]      
            
        return

    def get_currently_playing(self, oauth):
        query = 'https://api.spotify.com/v1/me/player/currently-playing'
        response = requests.get(query,
                                 headers = {'content-Type':'application/jsson',
                                 'Authorization':'Bearer {}'.format(oauth)}
                                 )
        return response.json()
    def go_live(self):
        token = input('If you do not have an Oauth token available please go to https://developer.spotify.com/console/get-user-player/.\n Follow the steps and nter your token here: ')
        currently_playing = ''
        playing = True
        while playing:
            track = self.get_currently_playing(token)
            if track['item']['uri'] != currently_playing:
                currently_playing = track['item']['uri']
                ##INTERFACING WITH VOD PLAYER
                #GET URI OF WHAT CURENTLY PLAYING AND OPEN AND PLAY THE VOD
                #for now just display currently playing info
                name = track['item']['name']
                artist = track['item']['artists'][0]['name']
                album = track['item']['album']['name']
                print('{}\n{}\n{}'.format(name,album,artist))


a = SaveSongs()
# #a.find_songs()
# a.get_song_features()
# #info = a.track_dict
# info = a.track_analysis

# print(a.tracks_name[1],info[a.tracks_name[1]])
# #print(a.get_curretly_playing())
a.go_live()
