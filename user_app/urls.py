
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.api.urls') ),
    path('profile/', include('user_profile.api.urls') ),
    path('watch/', include('watch_app.api.urls'))

]
