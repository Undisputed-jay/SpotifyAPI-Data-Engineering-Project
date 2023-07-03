import json
import boto3
import os
from datetime import datetime
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def lambda_handler(event, context):
    
    client = boto3.client('s3')
    
    x = os.environ['client_id']
    y = os.environ['client_secret']
    
    client_credentials_manager = SpotifyClientCredentials(client_id = x, client_secret = y)
    
    sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)
    
    playlist = "https://open.spotify.com/playlist/37i9dQZF1DX4W3aJJYCDfV"
    
    playlist_URI = playlist.split('/')[-1]
    
    result = sp.playlist_tracks(playlist_URI)
    
    filename = 'spotify_raw' + str(datetime.now()) + '.json'
    
    df = json.dumps(result)
    
    data = client.put_object(
        Bucket = 'spot-etl-project',
        Key = 'raw_data/to_processed/' + filename,
        Body = df)
    
    
