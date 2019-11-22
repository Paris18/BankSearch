from django.db import models

# Create your models here.

class TimeStampedModel(models.Model):
	'''abstract model for all models with created,updated,active user columns'''
	is_active = models.BooleanField(default=True)
	updated_at = models.DateTimeField(auto_now_add=True)
	created_at = models.DateTimeField(auto_now = True)

	class Meta:
		abstract=True

