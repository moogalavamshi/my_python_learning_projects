import random
import urllib.request
import requests
from bs4 import BeautifulSoup

def download_image(url):
    name = random.randrange(1, 1000)
    fullname = str(name) + ".jpg"
    urllib.request.urlretrieve(url, fullname)

def downloader():

    url = "http://www.geckoandfly.com/13248/40-free-motivational-inspirational-quotes-wallpapers-posters/"
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    for link in soup.findAll('img', {}):
        href = link.get('src')
        download_image(href)

downloader()