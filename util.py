from json import load
from instagrapi import Client
from dotenv import load_dotenv
import os
import time

def login():
    cl=Client()
    load_dotenv()
    cl.login(os.getenv('user_id'),os.getenv('password'))
    print('Login Successful')
    return cl


def fetch_reels(cl,url):
    
    id=cl.media_pk_from_url(url)
    address=cl.video_download(id)
    return address

