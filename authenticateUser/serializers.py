from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import get_user_model as User


class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User()
        fields = ['name', 'email']


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        print(attrs)
        data = super().validate(attrs)
        print(data)
        serializer = UserDetailsSerializer(self.user).data
        print(serializer, "fafdadfasfd")

        for k, v in serializer.items():
            data[k] = v
        # data['username'] = self.user.name
        # data['email'] = self.user.email

        return data


class UserCreateSerializer(serializers.ModelSerializer, MyTokenObtainPairSerializer):
    password1 = serializers.CharField(required=True, write_only=True)
    refresh = serializers.CharField(read_only=True)
    access = serializers.CharField(read_only=True)

    class Meta:
        model = User()
        fields = ['name', 'email', 'password', 'password1', 'refresh', 'access']
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, attrs):
        if attrs['password1'] != attrs['password']:
            raise serializers.ValidationError({'password': "Password Don't match"})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password1')
        user = User().objects.create_user(**validated_data)
        validated_data.pop('name')
        print("Create call")
        data = MyTokenObtainPairSerializer.validate(self, validated_data)
        print(data)

        return data
