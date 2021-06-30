from rest_framework import serializers
from watchlist_app.models import User

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        