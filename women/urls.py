from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('home/', index, name='home'),
    path('cats/<int:catid>/', categories),
]