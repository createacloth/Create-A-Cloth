from django.urls import path
from . import views
#. = current directory

urlpatterns = [
    path('', views.index, name='index')
]
#views.index returns function index from views.py
