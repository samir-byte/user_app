from django.urls import path
from user_profile.api.views import profile_view


urlpatterns = [
    path('', profile_view, name='profile' )

]