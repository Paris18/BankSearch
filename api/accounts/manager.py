from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):

	def create_user(self,mobile,email,password=None,**extra_fields):
		user = self.model(
			mobile = mobile,
			email = email,
			**extra_fields
			)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self,email,password,**extra_fields):
		mobile = ""
		user = self.create_user(
			mobile,
			email,
			password = password,
			**extra_fields)
		user.is_superuser = True
		user.save(using=self._db)
		return user