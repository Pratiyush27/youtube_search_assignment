from django.shortcuts import render
from .models import Search
import requests
import json

def populate_db():

    Search.objects.all().delete()
    api_key = 'AIzaSyDrdOoGUmwWKKtKJDjKBspekUjnzSBUCZI'
    link = 'https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=100&order=date&q=football&key='+ api_key

    data = requests.get(link).json()
    for search in data['items']:
        Vid_id = search['id']['videoId']
        snippet = search['snippet']
        Title = snippet['title']
        Published_at = snippet['publishedAt']
        Description = snippet['description']
        Thumbnail = snippet['thumbnails']['medium']
        Thumbnail_url = Thumbnail['url']

        new_search = Search(vid_id=Vid_id, title=Title, description=Description, published_at=Published_at, thumbnail_url=Thumbnail_url)
        new_search.save()


# Create your views here.
def index(request):

    populate_db()

    all_videos = Search.objects.all()
    print(all_videos)
    return render(request)