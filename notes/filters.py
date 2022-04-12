from django_filters import rest_framework as filters
from .models import Note

class NoteFilter(filters.FilterSet):
    
    name = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = Note
        fields = ['name']