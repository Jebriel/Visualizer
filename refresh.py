import secrets
import requests
import json

class Refresh:
    def __init__(self):
        self.refresh_token = secrets.stuff['refresh_token']
        self.base64 = secrets.base64
        self.newToken = self.refresh()

    def refresh(self):
        query = 'https://accounts.spotify.com/api/token'
        response = requests.post(query,
                                data = {'grant_type':'refresh_token', 
                                'refresh_token':self.refresh_token},
                                headers = {'Authorization':'Basic '+self.base64}
                                )
        return response.json()['access_token']
print(Refresh().newToken)

