from rest_framework import generics
from app.product.models import DisplayCode, Points
from app.product.serializers import DisplayCodeSerializer, PointsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from app.TG.CodeFromDisplay import encode_in_message_on_display, get_lasts, way
from sqlite3 import *
from random import *
import os


class GetListAllDisplayCodeProduct(generics.ListAPIView):
    serializer_class = DisplayCodeSerializer

    def get_queryset(self):
        return DisplayCode.objects.all()


class GetListAllPoints(generics.ListAPIView):
    serializer_class = PointsSerializer

    def get_queryset(self):
        return Points.objects.all()


class CreateDisplayCode(APIView):

    def post(self, request, format=None):
        print('test', way)

        text = request.data.get('text')
        message = encode_in_message_on_display(text)
        print(f'{text} - {message}')

        return Response(message, status=status.HTTP_201_CREATED)

