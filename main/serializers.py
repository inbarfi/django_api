from rest_framework import serializers
from .models import Audio

class AudioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Audio
        fields = ('id', 'url', 'title', 'language', 'good_quality')
