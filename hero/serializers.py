from rest_framework import serializers

from .models import HeroModel, HeroWorkList, HeroFeaturedProject

class HeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroModel
        fields = '__all__'

class HeroWorkListSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroWorkList
        fields = '__all__'
class HeroFeaturedProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroFeaturedProject
        fields = '__all__'