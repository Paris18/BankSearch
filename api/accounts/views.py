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
					User,
					)
from .serializers import (
	UserLoginRequestSerializer,
	# UserVerifyRequestSerializer,
	# UserSerializer,
	UserRegSerializer,
	UserListSerializer,
	UserUpdateRequestSerializer,
)

class UserViewSet(GenericViewSet):
	"""
	"""
	# queryset = User.objects.all()
	# filter_backends = (filters.OrderingFilter,)
	# authentication_classes = (TokenAuthentication,)

	ordering_fields = ('id',)
	ordering = ('id',)
	lookup_field = 'id'
	http_method_names = ['get', 'post', 'put']
	model = User

	def get_queryset(self):
		return User.objects.all()


	serializers_dict = {
		'login': UserLoginRequestSerializer,
		'register': UserRegSerializer,
		'listusers': UserListSerializer,
		'userupdate': UserUpdateRequestSerializer,
	}

	def get_serializer_class(self):
		"""
		"""
		try:
			return self.serializers_dict[self.action]
		except KeyError as key:
			raise 

	@action(methods=['post'], detail=False)
	def register(self,request):
		'''register user data'''

		serializer = self.get_serializer(data = request.data)
		if serializer.is_valid() is False:
			Response(serializer.errors,404)
		user = serializer.create(serializer.data)
		if user:
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response({}, status.HTTP_200_OK)

	@action(methods=['get'],detail=False, permission_classes=[IsAuthenticated, ])
	def listusers(self,request):
		serializer = self.get_serializer(self.get_queryset(),many=True)
		return Response(serializer.data, status.HTTP_200_OK)

	@action(methods=['post'], detail=False)
	def login(self, request):
		serializer = self.get_serializer(data=request.data)
		if serializer.is_valid() is False:
			Response(serializer.errors,404) 
		user = authenticate(
			email=serializer.data["email"],
			password=serializer.data["password"])
		if not user:
			return Response({'error': 'Invalid Credentials'},
							status=404)
		return Response({},
						status=status.HTTP_200_OK)

	@action(methods=['put'], detail=False, permission_classes=[IsAuthenticated, ])
	def userupdate(self, request):
		user_instance = User.objects.get(id=request.user.id)
		serializer = self.get_serializer(user_instance,data=request.data)
		if serializer.is_valid() is False:
			Response(serializer.errors,404) 
		user = serializer.save()
		return Response(serializer.data,
						status=status.HTTP_200_OK)

