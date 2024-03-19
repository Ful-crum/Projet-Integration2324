from django.db import models
from .representation import *
from .user import *

class Representation_user(models.Model):
    representation = models.ForeignKey(Representation, on_delete=models.SET_NULL, null=True, related_name='representations_user')
    user = models.ForeignKey(User, on_delete=models.SET_NULL , null=True, related_name='representations_user')
    places = models.IntegerField

    class Meta:
       db_table = "representations_user"