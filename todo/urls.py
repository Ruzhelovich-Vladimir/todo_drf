"""todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework.routers import DefaultRouter

# from participants.views import ParticipantModelViewSets
from notes.views import NoteMotelViewSet
from projects.views import ProjectModelViewSet, DevelopmentModelViewSet

# router = DefaultRouter()
# # router.register('participants', ParticipantModelViewSet)
# # router.register('projects', ProjectModelViewSet)
# router.register('developments', DevelopmentModelViewSet)
# router.register('nodes', NodeModelViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    # path('api/', include(router.urls)),
    path('nodes/', include('notes.urls')),
    path('participants/', include('participants.urls')),
    path('projects/', include('projects.urls'))
]
