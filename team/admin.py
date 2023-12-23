from django.contrib import admin

# Register your models here.
from .models import TeamModel, ServicesModel, ProjectsModel, TestiminoalsModel
class TeamAdmin(admin.ModelAdmin):
    list_display = ('teamCardImage', 'teamCardTitle', 'teamCardFbLink', 'teamCardTwitterLink', 'teamCardInstagramLink')

class ServicesAdmin(admin.ModelAdmin):
    list_display = ('servicesCardTitle', 'servicesCardDescription', 'servicesCardImage1', 'servicesCardImage2', 'servicesCardImage3', 'servicesCardImage4')

class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('projectImage', 'projectTitle')

class TestiminoalsAdmin(admin.ModelAdmin):
    list_display = ('testiminoalsCardImage', 'testiminoalsCardTitle', 'testiminoalsCardDescription', 'testiminoalsCardDesignation')

admin.site.register(ProjectsModel, ProjectsAdmin)
admin.site.register(TeamModel, TeamAdmin)
admin.site.register(ServicesModel, ServicesAdmin)
admin.site.register(TestiminoalsModel, TestiminoalsAdmin)