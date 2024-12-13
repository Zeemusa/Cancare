from django.urls import path, include
from . import views

urlpatterns = [
   path('', views.homepage, name='homepage'),
   path('cancer/',views.cancer, name='types'),
   path('cancer/<int:pk>', views.disease, name='disease')
]