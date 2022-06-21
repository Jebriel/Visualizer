

'''
Step 1: take the url and copy paste to browser
Step 2: from the redirect page copy the code portion in the url
Step 3: Take the 'code' and paste into the code part of the curl command
Step 4: Take the cliend_ID and client_secret and paste as id:secret then encode to base 64
Step 4b: Take the coded line and paste in the curls Authorization field
Step 5: past the curl command into terminal and copy output to 'stuff'
'''

spotify_user_id = 'tehag1'
playlist_id = '6AZmhUUSzUszsJa31LD47w'#'6AZmhUUSzUszsJa31LD47w'6sZB9Sxg09K2cJVCD3pKrg

base64 = 'NTNiZGNjZGE2NDEyNDU4MjljOWRhZWE2ZmM4NzhhYmI6ZWI4NDNkZTU2MTkyNDExZTlhZjk3OTc5Yjk2OWExZjM='

stuff = {"access_token":"BQAkNfVS4YjCy0Lht2tSi_WS_1KL_JsD4dzXec5dukdJsQsFdisaCYVRSk86-F5p2knT8BoTo9qWs1msj0198qzKvPVhhjhceS6QoWPVeh6wJzoBd4rwDd5eTiX_fjyR_Ry_2-aOjX_J",
"token_type":"Bearer",
"expires_in":3600,
"refresh_token":"AQC3A07MIvUvu4xQlJE1lAsMH8sOVzOJnkUjToCR6JxHwQhip6nHmdWBF1wH7tho9mgSSVAb_7FUzTKe5JLUnrKyO8dF91ZKv0GQFwu1YkdynkmeZQ2t60k6aWZ3qgfoDvk"}

