
from django.urls import path
from accounts.api.views import RegistrationView, LogoutView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register/', RegistrationView, name='register' ),
    path('login/', obtain_auth_token, name='login'),
    path('logout/', LogoutView, name='logout'),

]