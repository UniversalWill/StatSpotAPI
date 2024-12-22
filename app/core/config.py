from dotenv import dotenv_values
from pathlib import Path

dotenv_path = Path('../../.env')
config = dotenv_values(dotenv_path=dotenv_path)

class Setting:
    def __init__(self):
        self.SPOTIFY_CLIENT_ID = config.get('SPOTIFY_CLIENT_ID')
        self.SPOTIFY_REDIRECT_ID = config.get('SPOTIFY_REDIRECT_ID')

settings = Setting()
