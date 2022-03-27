from django_filters import rest_framework as filters
from .models import Participant


class ParticipantFilter(filters.FilterSet):

    name = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = Participant
        fields = ['first_name']
