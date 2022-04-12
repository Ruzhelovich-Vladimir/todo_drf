
from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from rest_framework import serializers

from participants.models import Participant
from participants.serializers import ParticipantModelSerializer
from .models import Project, Development


# class ProjectModelSerializer(ModelSerializer):
class ProjectModelSerializer(ModelSerializer):
    """ Серилизатор проекта """
    project_manager = ParticipantModelSerializer()

    # project_manager = UserModelSerializer()
    class Meta:
        model = Project
        fields = '__all__'


# class DevelopmentModelSerializer(ModelSerializer):
class DevelopmentModelSerializer(ModelSerializer):
    """ Серилизатор разработчики """
    project = ProjectModelSerializer(many=False)
    development = ParticipantModelSerializer(many=False)

    class Meta:
        model = Development
        fields = '__all__'
