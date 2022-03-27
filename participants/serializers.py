from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from .models import Participant

class ParticipantHyperlinkedModelSerializer(HyperlinkedModelSerializer):
    """ Серелизатор пользователя """

    class Meta:
        model = Participant
        # fields = '__all__'
        exclude = ['is_activate', 'updated_at']


class ParticipantModelSerializer(ModelSerializer):
    """ Серелизатор пользователя """

    class Meta:
        model = Participant
        # fields = '__all__'
        exclude = ['is_activate', 'updated_at']

