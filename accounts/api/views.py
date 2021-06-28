from accounts.api.serializers import RegistrationSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status

@api_view(['POST'])
def RegistrationView(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data = request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = 'Registration successful'
            data['username'] = account.username
        else:
            data = serializer.errors
    return Response(data)

@api_view(['POST'])
def LogoutView(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
    return Response({"success":("Successfully logged out.")},
                    status=status.HTTP_200_OK)