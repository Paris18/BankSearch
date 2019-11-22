# django imports
from rest_framework import filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework import status
# from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
# from rest_framework.pagination import PageNumberPagination
from django.contrib.auth import authenticate

# app level imports
from .models import (
					Banks,
					Branches,
					)
from .serializers import (
	BankListSerializer,
)

class BanksViewSet(GenericViewSet):
	"""
	"""
	# queryset = User.objects.all()
	# filter_backends = (filters.OrderingFilter,)
	# authentication_classes = (TokenAuthentication,)

	ordering_fields = ('id',)
	ordering = ('id',)
	lookup_field = 'id'
	http_method_names = ['get', 'post', 'put']
	model = Branches

	def get_queryset(self,filters = None):
		queryset =  self.model.objects.all()
		if filters:
			queryset = queryset.filter(**filters)
		return queryset


	serializers_dict = {
		'listbanks': BankListSerializer,
		'getbank':BankListSerializer
	}

	def get_serializer_class(self):
		"""
		"""
		try:
			return self.serializers_dict[self.action]
		except KeyError as key:
			raise 

	@action(methods=['get'],detail=False, permission_classes=[IsAuthenticated, ])
	def listbanks(self,request):
		filters = request.query_params.dict()
		try:
			filters.pop("limit")
			filters.pop("offset")
		except:
			pass
		pages = self.paginate_queryset(self.get_queryset(filters=filters))
		serializer = self.get_serializer(pages,many=True)
		return self.get_paginated_response(serializer.data)

	@action(methods=['get'],detail=False, permission_classes=[IsAuthenticated, ])
	def getbank(self,request):
		try:
			ifsc = request.GET.get('ifsc')
			bank = self.get_queryset().get(ifsc=ifsc)
			serializer = self.get_serializer(bank)
			return Response(serializer.data,status.HTTP_200_OK)
		except self.model.DoesNotExist:
			Response(serializer.errors,404) 



