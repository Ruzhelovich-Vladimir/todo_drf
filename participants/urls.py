from django.urls import path
from django.conf.urls import include
from rest_framework.routers import DefaultRouter
from participants.views import ParticipantModelViewSet

router_participants = DefaultRouter()
router_participants.register('', ParticipantModelViewSet, basename='participant')

urlpatterns = [
    path('', include(router_participants.urls)),
    path('<str:name>/', include(router_participants.urls)),
]
