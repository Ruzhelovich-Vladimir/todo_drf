from rest_framework.viewsets import ModelViewSet
from .models import Participant
from .serializers import ParticipantModelSerializer


class ParticipantModelViewSet(ModelViewSet):

    queryset = Participant.objects.all()

    serializer_class = ParticipantModelSerializer