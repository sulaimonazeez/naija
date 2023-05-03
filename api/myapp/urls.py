from django.urls import path,re_path
from . import views
from django.conf.urls import handler404
urlpatterns = [
  path("post", views.poster, name="poster"),
  path("", views.home, name="home"),
  path("music/<int:id>", views.handle_object, name="music_id"),
  path('music', views.music, name="music"),
  path("movie", views.video, name='video'),
  path("news", views.new, name="new"),
  path('news/<int:id>', views.get_new, name="get_news"),
  path("artist/<int:id>", views.get_artist, name='get_artist'),
  path('movie/<int:id>', views.get_video, name="get_video"),
  re_path(r'^media/(?P<path>.+)$', views.serve_static_file),
  re_path(r'^(?!media|static|artist|music|news|movie).*$', views.not_found, name='not_found'),
]


