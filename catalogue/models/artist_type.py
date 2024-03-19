from django.db import models
from .artist  import *
from .type import *


# Create your models here.
class Artist_type(models.Model):
	artist = models.ForeignKey(Artist, on_delete=models.SET_NULL , null=True, related_name='artiste_type')
	type = models.ForeignKey(Type, on_delete=models.SET_NULL , null=True, related_name='artiste_type')
	
	class Meta:
		db_table = "artiste_type"