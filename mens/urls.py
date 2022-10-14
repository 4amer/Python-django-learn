from django.urls import path
from .views import *

urlpatterns = [
    path('', bruh),
    path('into/<int:Br>', into)
]