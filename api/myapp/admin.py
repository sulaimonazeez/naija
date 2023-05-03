from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.musicUploaders)
admin.site.register(models.Movies)
admin.site.register(models.trendingArtists)
admin.site.register(models.topArtists)
admin.site.register(models.New)