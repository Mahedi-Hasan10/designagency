from django.contrib import admin
from . import models
# Register your models here.

class HeroWorkListAdmin(admin.ModelAdmin):
    list_display = ('workTitle', 'workCardImage', 'workCardTitle', 'workCardText', 'workCardImage2', 'workCardCount', 'workCardText2')
class HeroFeaturedProjectAdmin(admin.ModelAdmin):
    list_display = ('featuredTitle', 'featuredProjectImage', 'featuredProjectTitle', 'featuredProjectText', 'featuredProjectDate')
class HeroModelAdmin(admin.ModelAdmin):
    list_display = ('logo', 'heroTitle', 'heroText', 'hero_image1', 'hero_image2', 'hero_image3', 'hero_image4', 'hero_com_image1', 'hero_com_image2', 'hero_com_image3', 'hero_com_image4')

admin.site.register(models.HeroModel, HeroModelAdmin)
admin.site.register(models.HeroWorkList, HeroWorkListAdmin)
admin.site.register(models.HeroFeaturedProject, HeroFeaturedProjectAdmin)
