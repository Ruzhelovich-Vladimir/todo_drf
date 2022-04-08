from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer

from notes.models import Note
from participants.serializers import ParticipantModelSerializer
from projects.serializers import ProjectModelSerializer


class NoteModelSerializer(ModelSerializer):
    project = ProjectModelSerializer()
    author = ParticipantModelSerializer()

    class Meta:

        model = Note
        fields = '__all__'
