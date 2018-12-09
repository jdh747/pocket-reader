import functools
import requests
import configparser

# Load API keys
# To get API keys, follow instructions here: https://getpocket.com/developer/docs/authentication
config = configparser.ConfigParser()
config.read('config.ini')
CONSUMER_KEY = config['DEFAULT']['CONSUMER_KEY']
ACCESS_TOKEN = config['DEFAULT']['ACCESS_TOKEN']

BASE_URL = "https://getpocket.com"


def post(url):
    def decorator_post(func):
        @functools.wraps(func)
        def wrapper_post(*args, **kwargs):
            params = func(*args, **kwargs)
            params['consumer_key'] = CONSUMER_KEY
            params['access_token'] = ACCESS_TOKEN
            return requests.post(url, data=params)
        return wrapper_post
    return decorator_post


"""
Fetches unread articles from the Pocket /v3/get API.

Returns:
    requests.models.Response -- A response object generated from the Pocket /v3/get API.
"""


@post(f"{BASE_URL}/v3/get")
def fetch_unread_articles():
    return {
        'state': 'unread',
        'contentType': 'article',
        'detailType': 'simple'
    }
