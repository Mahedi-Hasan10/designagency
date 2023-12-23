from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

from django.conf import settings
from django.conf.urls.static import static

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'team', views.TeamViewSet,basename="team")
router.register(r'services', views.ServicesViewSet,basename="services")
router.register(r'projects', views.ProjectsViewSet,basename="projects")
router.register(r'testimonial', views.TestiminoalsViewSet,basename="testimonial")


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls))
 
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)