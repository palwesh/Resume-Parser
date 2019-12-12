from rest_framework import serializers
from .models import *

class FileSerializer(serializers.ModelSerializer):
    class Meta():
        model = Resume
        fields = '__all__'
