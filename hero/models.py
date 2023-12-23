from django.db import models

# Create your models here.
# create a model called hero section for all components of the hero section
class HeroModel(models.Model):
    logo = models.ImageField(upload_to='static/images/',  max_length=254)
    heroTitle = models.CharField(max_length=100)
    heroText = models.TextField()
    hero_image1 = models.ImageField(upload_to='static/images/hero/')
    hero_image2 = models.ImageField(upload_to='static/images/hero/')
    hero_image3 = models.ImageField(upload_to='static/images/hero/')
    hero_image4 = models.ImageField(upload_to='static/images/hero/')
    hero_com_image1 = models.ImageField(upload_to='static/images/hero/community/')
    hero_com_image2 = models.ImageField(upload_to='static/images/hero/community/')
    hero_com_image3 = models.ImageField(upload_to='static/images/hero/community/')
    hero_com_image4 = models.ImageField(upload_to='static/images/hero/community/')

class HeroWorkList(models.Model):
    workTitle = models.CharField(max_length=100)
    workCardImage = models.ImageField(upload_to='static/images/hero/worklist/')
    workCardTitle = models.CharField(max_length=100)
    workCardText = models.TextField()

    workCardImage2 = models.ImageField(upload_to='static/images/hero/worklist/')
    workCardCount = models.CharField(max_length=100)
    workCardText2 = models.TextField()

class HeroFeaturedProject(models.Model):
    featuredTitle = models.CharField(max_length=100)
    featuredProjectImage = models.ImageField(upload_to='static/images/hero/featuredproject/')
    featuredProjectTitle = models.CharField(max_length=100)
    featuredProjectText = models.TextField()
    featuredProjectDate = models.DateField(auto_now_add=True)
    