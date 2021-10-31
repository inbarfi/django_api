from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Audio
from .serializers import AudioSerializer

class AudioView(viewsets.ModelViewSet):
    #pulling data from db
    queryset = Audio.objects.all()
    # serializers convert db objects to and from json
    serializer_class = AudioSerializer