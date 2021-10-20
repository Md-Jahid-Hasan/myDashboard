from abc import ABC

from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import get_user_model as User


class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User()
        fields = ['name', 'email']


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        print(data)
        serializer = UserDetailsSerializer(self.user).data

        for k, v in serializer.items():
            data[k] = v
        # data['username'] = self.user.name
        # data['email'] = self.user.email

        return data