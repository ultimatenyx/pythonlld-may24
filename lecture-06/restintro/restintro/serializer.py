from rest_framework import serializers

from restintro.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        # fields = ['id', 'name', 'email', 'age']