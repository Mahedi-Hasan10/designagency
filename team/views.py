from django.shortcuts import render

# Create your views here.
from .models import TeamModel, ServicesModel, ProjectsModel, TestiminoalsModel
from rest_framework import viewsets
from .serializers import TeamSerializer, ServicesSerializer, ProjectsSerializer, TestiminoalsSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = TeamModel.objects.all().order_by('teamCardTitle')
    serializer_class = TeamSerializer
class ServicesViewSet(viewsets.ModelViewSet):
    queryset = ServicesModel.objects.all().order_by('servicesCardTitle')
    serializer_class = ServicesSerializer
class ProjectsViewSet(viewsets.ModelViewSet):
    queryset = ProjectsModel.objects.all().order_by('projectTitle')
    serializer_class = ProjectsSerializer
class TestiminoalsViewSet(viewsets.ModelViewSet):
    queryset = TestiminoalsModel.objects.all().order_by('testiminoalsCardTitle')
    serializer_class = TestiminoalsSerializer
    
