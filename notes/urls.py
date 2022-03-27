from django.urls import path
from django.conf.urls import include
from rest_framework.routers import DefaultRouter
from notes.views import NoteMotelViewSet


router_notes = DefaultRouter()
router_notes.register('', NoteMotelViewSet, basename='note')

urlpatterns = [
    path('', include(router_notes.urls)),
    path('filter/<str:name>/', include(router_notes.urls)),
]
