from random import choice, choices
from string import ascii_letters, digits
from urllib.parse import urlencode
from fastapi import APIRouter
from fastapi.responses import RedirectResponse
from app.core.config import setting

router = APIRouter()

def generate_random_string(length: int) -> str:
    """
    generate random string for state RFC-6749
    
    Parametrs:
    lenght: lenght of generated string

    Return:
    random_string: random character string of length
    """

    random_string = ''.join(choices(ascii_letters + digits, k = length)) 

    return random_string

@router.get("/login")
async def login():
    state = generate_random_string(16)
    scope = 'user-read-private user-read-email'

    auth_url = 'https://accounts.spotify.com/authorize?' + urlencode({
        'response_type': 'code',
        'client_id': settings.SPOTIFY_CLIENT_ID,
        'scope': scope,
        'redirect_uri': settings.SPOTIFY_REDIRECT_URI,
        'state': state
        })

    return RedirectResponse(url=auth_url)


