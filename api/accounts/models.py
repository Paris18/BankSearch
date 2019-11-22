# python imports
import uuid
# import jwt
from datetime import datetime, timedelta


# django/rest_framwork imports
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _
from rest_framework.authtoken.models import Token
from django.utils import timezone
from django.conf import settings
# from django.contrib.postgres.fields import JSONField

# project level imports
from libs.models import TimeStampedModel
# from libs.clients import sms_client
# from libs.utils.otp import create_otp

# app level imports
from .manager import UserManager
# from accounts.constants import TOO_MANY_ATTEMPTS, INVALID_OTP

# third party imports
from model_utils import Choices
from jsonfield import JSONField


class User(AbstractBaseUser, PermissionsMixin, TimeStampedModel):
	"""
	User model represents the user data in the database.
	"""
	GENDER = Choices(
		('M', 'Male'),
		('F', 'Female'),
		('O', 'Other'),
	)

	mobile = models.BigIntegerField(
		validators=[
			MinValueValidator(5000000000),
			MaxValueValidator(9999999999),
		],
		unique=True,
		db_index=True,)


	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	first_name = models.CharField(max_length=64, blank=True)
	last_name = models.CharField(max_length=64, blank=True)
	email = models.EmailField(max_length=128, unique=True, db_index=True, blank=True)
	gender = models.CharField(choices=GENDER, max_length=1, blank=True)

	objects = UserManager()

	USERNAME_FIELD = 'email'

	class Meta:
		app_label = 'accounts'
		db_table = 'api_user'

	def __str__(self):
		return str(self.mobile)

	@property
	def full_name(self):
		return "{fn} {ln}".format(fn=self.first_name, ln=self.last_name)



	def save(self, *args, **kwargs):
		"""
		if has_django_dashboard_access is True, then setting is_staff to True
		"""

		# if self.has_django_dashboard_access is True:
		#     self.is_staff = True
		super(User, self).save(*args, **kwargs)
		

	def modify(self, payload):
		"""
		This method will update tasks attributes
		"""
		for key, value in payload.items():
			setattr(self, key, value)
		self.save()


