from django.urls import path, include
from . import views

urlpatterns = [
   path('', views.homepage, name='homepage'),
   path('types',views.types, name='types')
]