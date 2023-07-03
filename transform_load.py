import json
import boto3
import os
from datetime import datetime
import pandas as pd
from io import StringIO


def lambda_handler(event, context):
    
    Bucket = 'spot-etl-project'
    Key = 'raw_data/to_processed/'
    
    client = boto3.client('s3')
    
    spotify_data = []
    spotify_key = []
    
    for file in client.list_objects(Bucket = Bucket, Prefix = Key)['Contents']:
        file_key = file['Key']
        if file_key.split('.')[-1] == 'json':
            response = client.get_object(Bucket = Bucket, Key = file_key)
            
            response_body = response['Body']
            result = json.loads(response_body.read())
            
            result_item = result['items']
            
            
    artist_ID = []
    song_ID = []
    album_ID = []
    album_name = []
    artist_name = []
    release_date = []
    total_tracks = []
    url = []
    duration = []
    popularity = []
    exp = []
    uri = []
    ext_uri = []
    song_time = []
    song_name = []
    
    for result in result_item:
        try:
            artist_ID.append(result['track']['id'])
        except:
            artist_ID.append('n/a')
        try:
            song_ID.append(result['track']['album']['artists'][0]['id'])
        except:
            song_ID.append('n/a')
        try:
            album_ID.append(result['track']['album']['id'])
        except:
            album_ID.append('n/a')
        try:
            album_name.append(result['track']['album']['name'])
        except:
            album_name.append('n/a')
        try:
            song_time.append(result['added_at'])
        except:
            song_time.append('n/a')
        try:
            artist_name.append(result['track']['artists'][0]['name'])
        except:
            artist_name.append('n/a')
        try:
            release_date.append(result['track']['album']['release_date'])
        except:
            release_date.append('n/a')
        try:
            total_tracks.append(result['track']['album']['total_tracks'])
        except:
            total_tracks.append('n/a')
        try:
            url.append(result['track']['album']['artists'][0]['external_urls']['spotify'])
        except:
            url.append('n/a')
        try:
            duration.append(result['track']['duration_ms'])
        except:
            duration.append('n/a')
        try:
            popularity.append(result['track']['popularity'])
        except:
            popularity.append('n/a')
        try:
            exp.append(result['track']['explicit'])
        except:
            exp.append('n/a')
        try:
            uri.append(result['track']['uri'])
        except:
            uri.append('n/a')
        try:
            ext_uri.append(result['track']['album']['href'])
        except:
            ext_uri.append('n/a')
        try:
            song_name.append(result['track']['name'])
        except:
            song_name.append('n/a')
            
    artist_element = {'Artist ID': artist_ID, 'Artiste': artist_name, 'External URL': ext_uri}
    album_element = {'Album ID': album_ID, 'Album Name': album_name, 'Release Date': release_date,
                            'Total Tracks': total_tracks, 'Track URI': uri}
    song_element = {'Song ID': song_ID, 'Total Tracks': total_tracks, 'Song Name': song_name, 'Popularity': popularity,
                           'Date Added': song_time, 'Duration': duration, 'Artist ID': artist_ID,'Album ID': album_ID}
    artist_df = pd.DataFrame(data = artist_element)
    album_df = pd.DataFrame(data = album_element)
    song_df = pd.DataFrame(data = song_element)
    
    song_df = song_df.drop_duplicates()
    album_df = album_df.drop_duplicates()
    artist_df = artist_df.drop_duplicates()
    
    song_df['Date Added'] = pd.to_datetime(song_df['Date Added'])
    
    artist_key = 'transformed_data/artist_data/artist' + str(datetime.now()) + '.csv'
    artist_buffer = StringIO()
    artist_df.to_csv(artist_buffer, index = False)
    artist_content = artist_buffer.getvalue()
    client.put_object(Bucket = Bucket, Key = artist_key, Body = artist_content)
    
    album_key = 'transformed_data/album_data/album' + str(datetime.now()) + '.csv'
    album_buffer = StringIO()
    album_df.to_csv(album_buffer, index = False)
    album_content = album_buffer.getvalue()
    client.put_object(Bucket = Bucket, Key = album_key, Body = album_content)
    
    song_key = 'transformed_data/song_data/album' + str(datetime.now()) + '.csv'
    song_buffer = StringIO()
    song_df.to_csv(song_buffer, index = False)
    song_content = song_buffer.getvalue()
    client.put_object(Bucket = Bucket, Key = song_key, Body = song_content)
                
                