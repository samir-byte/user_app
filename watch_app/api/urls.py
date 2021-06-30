
from django.urls import path
from watch_app.api.views import WatchListView, StreamPlatformListView


urlpatterns = [
    path('watchlist/', WatchListView.as_view(), name='list' ),
    path('stream/', StreamPlatformListView.as_view(), name='stream-list')

]