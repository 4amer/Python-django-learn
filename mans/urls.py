from django.urls import path
from .views import *

urlpatterns = [
    path('', native),
    path('bruh/', bruh)
]