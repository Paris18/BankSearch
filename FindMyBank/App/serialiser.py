# Django Imports
from rest_framework import serializers


# App Level Imports
from .models import Branches,Banks



class BanknameSerializer(serializers.ModelSerializer):
	name = serializers.CharField()

	class Meta:
		model = Banks
		fields = ('name',)
		# fields = '__all__'


class BankSerializer(serializers.ModelSerializer):
	bank = serializers.SlugField(source = 'bank.name')

	class Meta:
		model = Branches
		fields = "__all__"

