from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import VoiceViewSet
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register('voice', VoiceViewSet )



urlpatterns = [
    path('', include(router.urls)),
] 