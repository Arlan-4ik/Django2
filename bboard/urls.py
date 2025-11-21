from django.urls import path, include

from bboard.views import index

urlpatterns = [
    path('', index),
]
