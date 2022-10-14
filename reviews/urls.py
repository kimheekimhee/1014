from . import views
from django.urls import path

app_name = 'reviews'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
]