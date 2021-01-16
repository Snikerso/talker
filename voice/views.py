from django.shortcuts import render
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Voice
from .serializers import  VoiceSerializer
from rest_framework import status

class  VoiceViewSet(viewsets.ModelViewSet):
    queryset = Voice.objects.all()
    serializer_class = VoiceSerializer

    def get_queryset(self, *args, **kwargs):

        qs = Voice.objects.all()
        return qs