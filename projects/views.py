from rest_framework.viewsets import ModelViewSet
from .models import Project, Development
from .serializers import ProjectModelSerializer, DevelopmentModelSerializer
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import status
from rest_framework.response import Response
from django.http import Http404

class ProjectLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 2

class ProjectModelViewSet(ModelViewSet):

    queryset = Project.objects.all() #.filter(is_activate=True)
    serializer_class = ProjectModelSerializer
    filterset_fields = ['name']
    pagination_class = ProjectLimitOffsetPagination

    def destroy(self, request, *args, **kwargs):
        """" Помечаем запись как не активную """
        try:
            instance = self.get_object()
            Project.objects.all().filter(is_activate=True).filter(uid=instance.pk).update(is_activate=False)
        except Http404:
            pass
        return Response(status=status.HTTP_200_OK)

    # def get_queryset(self):
    #     queryset = Project.objects.all() #.filter(is_activate=True)
    #     pagination_class = ProjectLimitOffsetPagination
    #
    #     # Фильтр в запросе
    #     if 'name' in self.request.query_params:
    #         # В параметрах может быть только несколько значений
    #         for search_elem in self.request.query_params['name']:
    #             queryset = queryset.filter(name__contains=search_elem)
    #     # Фильтр в заголовке запроса
    #     if 'name' in self.request.headers:
    #         # В заголовке может быть только одно значение
    #         queryset = queryset.filter(
    #             name__contains=self.request.headers['name'])
    #     return queryset


class DevelopmentModelViewSet(ModelViewSet):

    queryset = Development.objects.all()
    serializer_class = DevelopmentModelSerializer
