from .models import musicUploaders,Movies, New
from datetime import datetime 
from django.db.models import Q
class Search(object):
  def __init__(self, inp):
    self.database = musicUploaders
    self.search = inp
  
  def search_data(self):
    result = []
    search = self.search.split()
    for i in range(len(search)):
      data = self.database.objects.filter(Q(titles__icontains=search[i])|Q(artists__icontains=search[i]))
      if data is not None:
        result = data
        break
    return result


class videoSearch(object):
  def __init__(self, inp):
    self.database = Movies
    self.search = inp
  
  def search_data(self):
    result = []
    search = self.search.split()
    for i in range(len(search)):
      data = self.database.objects.filter(titles__icontains=search[i])
      if data is not None:
        result = data
        break
    return result

class newSearch(object):
  def __init__(self, inp):
    self.database = New
    self.search = inp
  
  def search_data(self):
    result = []
    search = self.search.split()
    for i in range(len(search)):
      data = self.database.objects.filter(Q(title__icontains=search[i])|Q(new__icontains=search[i]))
      if data is not None:
        result = data
        break
    return result

def new_song():
  x = datetime.now()
  y = musicUploaders.objects.filter(dates=str(x.year))
  if len(y) < 5:
    return musicUploaders.objects.all()[:20]
  return y[: 20]
  
def new_video():
  x = datetime.now()
  y = Movies.objects.filter(dates=str(x.year))
  if len(y) < 5:
    return Movies.objects.all()[:20]
  return y[: 20]
  