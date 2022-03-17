from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Participant

class ParticipantModelSerializer(HyperlinkedModelSerializer):
    """ Серелизатор пользователя """

    class Meta:
        model = Participant
        fields = '__all__'
