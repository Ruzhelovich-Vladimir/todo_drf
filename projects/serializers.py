
from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from .models import Project, Development


# class ProjectModelSerializer(ModelSerializer):
class ProjectModelSerializer(HyperlinkedModelSerializer):
    """ Серилизатор проекта """

    # project_manager = UserModelSerializer()
    class Meta:
        model = Project
        fields = '__all__'


# class DevelopmentModelSerializer(ModelSerializer):
class DevelopmentModelSerializer(HyperlinkedModelSerializer):
    """ Серилизатор проекта """

    class Meta:
        model = Development
        fields = '__all__'
