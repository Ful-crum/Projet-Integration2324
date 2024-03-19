from django.db import models
from .artist_type  import *
from .show_ import *


# Create your models here.
class Artist_type_show(models.Model):
	artist_type_show = models.ForeignKey(Artist, on_delete=models.SET_NULL , null=True, related_name='artiste_type_show')
	show = models.ForeignKey(Show, on_delete=models.SET_NULL , null=True, related_name='artiste_type_show')
	
	class Meta:
		db_table = "artiste_type_show"