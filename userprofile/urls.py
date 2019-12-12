from django.conf.urls import url
from .views import *
from django.urls import path

urlpatterns = [
    path('upload/', FileView.as_view(), name='resume_upload'),
]
