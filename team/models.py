from django.db import models

# Create your models here.

class TeamModel(models.Model):
    teamCardImage = models.ImageField(upload_to='static/images/team')
    teamCardTitle = models.CharField(max_length=100)
    teamCardFbLink = models.CharField(max_length=100)
    teamCardTwitterLink = models.CharField(max_length=100)
    teamCardInstagramLink = models.CharField(max_length=100)

class ServicesModel(models.Model):
    servicesCardTitle = models.CharField(max_length=100)
    servicesCardDescription = models.CharField(max_length=300)
    servicesCardImage1 = models.ImageField(upload_to='static/images/services')
    servicesCardImage2 = models.ImageField(upload_to='static/images/services')
    servicesCardImage3 = models.ImageField(upload_to='static/images/services')
    servicesCardImage4 = models.ImageField(upload_to='static/images/services')

class ProjectsModel(models.Model):
    projectImage = models.ImageField(upload_to='static/images/projects')
    projectTitle = models.CharField(max_length=100)

class TestiminoalsModel(models.Model):
    testiminoalsCardImage = models.ImageField(upload_to='static/images/testiminoals')
    testiminoalsCardTitle = models.CharField(max_length=100)
    testiminoalsCardDescription = models.CharField(max_length=300)
    testiminoalsCardDesignation = models.CharField(max_length=100)
