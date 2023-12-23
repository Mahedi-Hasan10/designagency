from .models import TeamModel, ServicesModel, ProjectsModel, TestiminoalsModel
from rest_framework import serializers
class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamModel
        fields = '__all__'

class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicesModel
        fields = '__all__'
class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectsModel
        fields = '__all__'
class TestiminoalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestiminoalsModel
        fields = '__all__'
    
