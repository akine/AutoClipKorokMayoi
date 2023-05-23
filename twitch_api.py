import os

from dotenv import load_dotenv
import requests


load_dotenv()

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')

# アクセストークンを取得
def get_access_token():
    url = 'https://id.twitch.tv/oauth2/token'
    payload = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'grant_type': 'client_credentials'
    }
    response = requests.post(url, params=payload)
    return response.json()['access_token']

# ビデオ情報を取得
def get_videos(user_id, access_token):
    url = f'https://api.twitch.tv/helix/videos?user_id={user_id}'
    headers = {
        'Client-ID': CLIENT_ID,
        'Authorization': f'Bearer {access_token}'
    }
    response = requests.get(url, headers=headers)
    return response.json()
