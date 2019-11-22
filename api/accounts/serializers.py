# django imports
from rest_framework import serializers
# from django.contrib.auth import get_user_model  # If used custom user model

# app level imports
from .models import (
                    User,
                    )



class UserLoginRequestSerializer(serializers.Serializer):
    """
    UserLoginSerializer
    """
    email = serializers.IntegerField(
        required=True,
        min_value=5000000000,
        max_value=9999999999
    )
    password = serializers.CharField(required=True, min_length=5)

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'mobile','email'
        )


class UserSerializer(serializers.ModelSerializer):
    """
    UserSerializer
    """
    # access_token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'mobile', 'access_token', 'sub_cluster',
            'is_verified', 'is_active', 'email', 'image_url'
        )

    def get_access_token(self, user):
        """
        returns users access_token
        """
        return user.access_token


class UserRegSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(required=False)
    password = serializers.CharField(required=True, min_length=5)
    first_name = serializers.CharField(required=True, min_length=2)
    last_name = serializers.CharField(required=True, min_length=2)
    mobile = serializers.IntegerField(
        required=True,
        min_value=5000000000,
        max_value=9999999999
    )
    # user_role = serializers.UUIDField()

    class Meta:
        model = User
        fields = ('id', 'password', 'email', 'first_name', 'last_name', 'mobile')
        write_only_fields = ('password',)
        read_only_fields = ('id',)

    def validate(self,data):
        return data


    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserListSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'mobile')

class UserUpdateRequestSerializer(serializers.Serializer):
    id = serializers.UUIDField(required=False)
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    mobile = serializers.IntegerField(required=False)
    is_active = serializers.BooleanField(required=False)
    is_staff = serializers.BooleanField(required=False)
    is_verified = serializers.BooleanField(required=False)
    is_mobile_verified = serializers.BooleanField(required=False)
    is_blocked = serializers.BooleanField(required=False)
    is_active = serializers.BooleanField(required=False)
    email = serializers.EmailField(required=False)
    gender = serializers.CharField(required=False)
    block_reason = serializers.CharField(required=False)
    image_url = serializers.CharField(required=False)
    # reporting_person = serializers.PrimaryKeyRelatedField(required=False)

    def validate(self,data):
        return data

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'mobile', 'is_active')
        write_only_fields = ('password',)
        read_only_fields = ('id',)

