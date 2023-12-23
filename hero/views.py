from django.shortcuts import render

# Create your views here.
from .serializers import HeroSerializer, HeroWorkListSerializer, HeroFeaturedProjectSerializer
from rest_framework import viewsets
from .models import HeroModel, HeroWorkList, HeroFeaturedProject

class HeroViewSet(viewsets.ModelViewSet):
    queryset = HeroModel.objects.all()
    serializer_class = HeroSerializer

class HeroWorkListViewSet(viewsets.ModelViewSet):
    queryset = HeroWorkList.objects.all()
    serializer_class = HeroWorkListSerializer

class HeroFeaturedProjectViewSet(viewsets.ModelViewSet):
    queryset = HeroFeaturedProject.objects.all()
    serializer_class = HeroFeaturedProjectSerializer

