from django.http import HttpResponse
from django.shortcuts import render
from .search_query import Search,videoSearch,newSearch, new_song, new_video
from .models import musicUploaders, Movies,trendingArtists, New
from .forms import postData
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
def poster(request):
  if request.method == "POST":
    x = postData(request.POST, request.FILES)
    if x.is_valid():
      x.save()
      return HttpResponse("saved")
    else:
      return HttpResponse("Error")
  x = postData
  return render(request, 'post.html', {'form':x})
  
#not scraping 
def home(request):
  results = []
  if request.method == "POST":
    x = request.POST['search']
    searched = Search(x)
    result = searched.search_data()
    if result:
      results = result
  video = Movies.objects.all()
  data = musicUploaders.objects.all()
  trend = trendingArtists.objects.all()[:22]
  return render(request, 'home.html', {"data":data, "movie":video[:30], "trend":trend, "search":results})
  
def music(request):
  results = []
  if request.method == "POST":
    x = request.POST['search']
    searched = Search(x)
    result = searched.search_data()
    if result:
      results = result
  data = musicUploaders.objects.all()
  trend = trendingArtists.objects.all()[:22]
  return render(request, 'music.html', {"data":data, "search":results, "trend":trend})
  
def video(request):
  results = []
  if request.method == "POST":
    x = request.POST['search']
    searched = videoSearch(x)
    result = searched.search_data()
    if result:
      results = result
  video = Movies.objects.all()
  trend = trendingArtists.objects.all()[:22]
  return render(request, 'video.html', {"movie":video[:30], "trend":trend, "search":results})
import os
from pathlib import Path
from django.http import HttpResponseNotFound, FileResponse
BASE_DIR = Path(__file__).resolve().parent.parent
def serve_static_file(request, path):
    # Get the full path to the requested file
    full_path = os.path.join(BASE_DIR, path)

    # If the file exists, return it as a FileResponse
    if os.path.exists(full_path):
        return FileResponse(open(full_path, 'rb'))

    # If the file does not exist, return a 404 response
    return HttpResponseNotFound()

def new(request):
  results = []
  if request.method == "POST":
    x = request.POST['search']
    searched = newSearch(x)
    result = searched.search_data()
    if result:
      results = result
  new = New.objects.all()[:20]
  trend = trendingArtists.objects.all()[:22]
  return render(request, 'news.html', {"new": new,"trend":trend, "search":results})

def handle_object(request, id):
  data = musicUploaders.objects.get(id=id)
  other = musicUploaders.objects.filter(artists=data.artists)
  latest = new_song
  trend = trendingArtists.objects.all()[:22]
  return render(request, 'music_id.html', {"trend":trend, "data":data, "other":other, "latest":latest})
  
def get_new(request, id):
  data = New.objects.get(id=id)
  trend = trendingArtists.objects.all()[:22]
  return render(request, 'get_new.html',{'trend': trend, 'data':data})
  
  
def get_artist(request, id):
  trend = trendingArtists.objects.all()[:22]
  x = trendingArtists.objects.get(id=id)
  return render(request, 'trend.html', {'data':x, "trend": trend, "trend":trend})
  
  
def get_video(request, id):
  data = Movies.objects.get(id=id)
  latest = new_video
  other = Movies.objects.filter(titles=data.titles)
  trend = trendingArtists.objects.all()[: 22]
  return render(request, 'video_id.html', {'data':data, "trend":trend, "latest":latest, "other":other})

def not_found(request):
  return HttpResponse("Server not found")

#no one will understand except pro