# django imports
from rest_framework import serializers
# from django.contrib.auth import get_user_model  # If used custom user model

# app level imports
from .models import (
                    Banks,
                    Branches,
                    )


class BankListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Branches
        fields = '__all__'
