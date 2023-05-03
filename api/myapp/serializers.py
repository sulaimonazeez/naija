from rest_framework import serializers
from .models import musicUploaders

class Serializer(serializers.ModelSerializer):
  class Meta:
    model = musicUploaders
    fields = '__all__'