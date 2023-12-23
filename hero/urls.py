from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

from django.conf import settings
from django.conf.urls.static import static

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'hero', views.HeroViewSet,basename="hero")
router.register(r'hero-feature', views.HeroFeaturedProjectViewSet,basename="hero-feature")
router.register(r'hero-worklist', views.HeroWorkListViewSet,basename="hero-work")

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls))
 
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)