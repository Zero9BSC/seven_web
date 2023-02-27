from django.urls import path
from Multimedia import views

urlpatterns = [
    path('multimedia', views.multimedia, name='Multimedia'),
]