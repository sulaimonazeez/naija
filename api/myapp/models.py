from django.db import models
from cloudinary.models import CloudinaryField
from cloudinary.models import CloudinaryField
import requests
class musicUploaders(models.Model):
  titles = models.CharField(max_length=255)
  dates = models.CharField(max_length=255)
  artists = models.CharField(max_length=255)
  albums = CloudinaryField('image')
  songs = CloudinaryField('file')
  class Meta:
    ordering = ('-id', )
  
  def __str__(self):
    return self.titles
    
class Movies(models.Model):
  artist_name = models.CharField(max_length=255)
  feature = models.CharField(blank=True,max_length=255)
  titles = models.CharField(max_length=255)
  date = models.CharField(max_length=255)
  albums = models.ImageField(upload_to='myapp/video')
  file = models.FileField(upload_to='myapp/video')
  
  class Meta:
    ordering = ('-id',)
  def __str__(self):
    return self.titles
  
class trendingArtists(models.Model):
  artist_realname = models.CharField(max_length=255)
  artist = models.CharField(max_length=255)
  record_label = models.CharField(max_length=255)
  genrie = models.CharField(max_length=255)
  bio = models.TextField(blank=True)
  image = models.ImageField(upload_to='myapp/bio')
  award = models.CharField(blank=True,max_length=255)
  def __str__(self):
    return self.artist
    
class topArtists(models.Model):
  artist_realname = models.CharField(max_length=255)
  artist = models.CharField(max_length=255)
  record_label = models.CharField(max_length=255)
  genrie = models.CharField(max_length=255)
  bio = models.TextField(blank=True)
  image = models.ImageField(upload_to='myapp/bio')
  award = models.CharField(blank=True,max_length=255)
  
  def __str__(self):
    return self.artist
    
class New(models.Model):
  title = models.CharField(max_length=1000)
  date = models.CharField(max_length=255)
  new = models.TextField()
  image = models.ImageField(upload_to='news')
  def __str__(self):
    return self.title
  class Meta:
    ordering = ('-id',)
    
class updateNew(models.Model):
  title = models.CharField(max_length=1000)
  bio = models.TextField(blank=False)
  img = models.ImageField(upload_to='myapp/static')
  date = models.CharField(max_length=255)
  class Meta:
    ordering = ('-id',)
  def __str__(self):
    return self.title
  
  
  