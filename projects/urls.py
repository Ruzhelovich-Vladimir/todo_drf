from django.urls import path
from django.conf.urls import include
from rest_framework.routers import DefaultRouter
from projects.views import ProjectModelViewSet

router_projects = DefaultRouter()
router_projects.register('', ProjectModelViewSet, basename='project')

urlpatterns = [
    path('', include(router_projects.urls)),
    path('filter/<str:name>/', include(router_projects.urls)),
]
