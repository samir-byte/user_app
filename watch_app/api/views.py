from rest_framework import generics
from watch_app.api.serializers import WatchListSerializer, StreamPlatformSerializer
from watch_app.models import WatchList, StreamPlatform

class WatchListView(generics.ListAPIView):
    queryset = WatchList.objects.all()
    serializer_class = WatchListSerializer

class StreamPlatformListView(generics.ListAPIView):
    serializer_class = StreamPlatformSerializer