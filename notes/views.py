from rest_framework.viewsets import ModelViewSet
from notes.models import Note
from notes.serializers import NoteModelSerializer
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import status
from rest_framework.response import Response
from django.http import Http404


class NoteLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20


class NoteMotelViewSet(ModelViewSet):

    queryset = Note.objects.all()
    #  .filter(is_activate=True)
    serializer_class = NoteModelSerializer
    pagination_class = NoteLimitOffsetPagination
    # filterset_fields = ['name', 'created']

    def destroy(self, request, *args, **kwargs):
        """" Помечаем запись как не активную """
        try:
            instance = self.get_object()
            Note.objects.all().filter(
                is_activate=True).filter(
                uid=instance.pk).update(
                is_activate=False)
        except Http404:
            pass
        return Response(status=status.HTTP_200_OK)

    def get_queryset(self):
        queryset = Note.objects.all()  # .filter(is_activate=True)
        pagination_class = NoteLimitOffsetPagination

        # Фильтр в запросе
        if 'name' in self.request.query_params:
            # В параметрах может быть только несколько значений
            for search_elem in self.request.query_params['name']:
                queryset = queryset.select_related('project').filter(
                    project__name__contains=search_elem)

        # Фильтр в заголовке запроса
        if 'name' in self.request.headers:
            # В заголовке может быть только одно значение
            queryset = queryset.select_related('project').filter(
                project__name__contains=self.request.headers['name'])

        # Фильтр в запросе
        if 'start_date' in self.request.query_params and 'end_date' in self.request.query_params:
            # В параметрах может быть только несколько значений
            start_date = self.request.query_params['start_date']
            end_date = self.request.query_params['end_date']
            queryset = queryset.filter(created_at__range=(start_date, end_date))

        # Фильтр в заголовке запроса
        if 'start_date' in self.request.headers and 'end_date' in self.request.headers:
            # В заголовке может быть только одно значение
            queryset = queryset.select_related('project').filter(
                created_at__range=(self.request.headers['start_date'], self.request.headers['end_date'])
            )

        return queryset
