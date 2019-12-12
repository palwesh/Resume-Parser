from django.shortcuts import render
from django.conf import settings

from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .serializers import FileSerializer

import re
import os

from pyresparser import ResumeParser
from .models import *



class FileView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    def post(self, request, *args, **kwargs):
        file_serializer = FileSerializer(data=request.data)
        if file_serializer.is_valid():
            file = file_serializer.validated_data['pdf']
            file_serializer.save()
            #using pyresparser library to extact the inffformation
            data = ResumeParser(file_serializer.instance.pdf.path).get_extracted_data()
            # print(data['name'], data['email'],data['mobile_number'])
            # print("_____________", data['skills'])
            userProfile.objects.create(
                user_name= data['name'],
                email_address= data['email'],
                phone_number= data['mobile_number'],
                skill= data['skills'],
            )
            file_serializer.save()

            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
