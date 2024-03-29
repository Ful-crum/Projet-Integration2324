"""reservations.catalogue URL Configuration
"""
from django.urls import path
from .views import *
from . import views

app_name='catalogue'

urlpatterns = [
    path('artist/', views.artist.index, name='artist_index'),
    path('artist/<int:artist_id>', views.artist.show, name='artist_show'),
    path('type/', views.type.index, name='type_index'),
    path('type/<int:type_id>', views.type.show, name='type_show'),
    path('locality/', views.locality.index, name='locality_index'),
    path('locality/<int:locality_id>', views.locality.show, name='locality_show'),
    path('role/', views.role.index, name='role_index'),
    path('role/<int:role_id>', views.role.show, name='role_show'),
    path('location/', views.location.index, name='location_index'),
	path('location/<int:location_id>', views.location.show, name='location_show'),
    path('show/', views.show_.index, name='show_index'),
    path('show/<int:show_id>', views.show_.show, name='show_show'),
    path('representation/', views.representation.index, name='representation_index'),
    path('representation/<int:show_id>', views.representation.show, name='representation_show'),

]