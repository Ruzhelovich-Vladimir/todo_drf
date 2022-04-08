from rest_framework.viewsets import ModelViewSet, ViewSet, GenericViewSet, mixins
from .models import Participant
from .serializers import ParticipantModelSerializer, ParticipantHyperlinkedModelSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework import mixins
from .filters import ParticipantFilter
from rest_framework.pagination import LimitOffsetPagination

""" Пример реализации через APIView"""
# class ParticipantView(APIView):
#
#     def get(self, request):
#         participants = Participant.objects.all().filter(is_activate=True)
#         serializer = ParticipantModelSerializer(participants, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         return Response("Ответ на POST-запрос ")


""" Пример реализации через шаблон прав APIView"""
# class ParticipantView(ListCreateAPIView):
#
#     queryset = Participant.objects.all().filter(is_activate=True)
#     serializer_class = ParticipantModelSerializer
#
#


""" Пример реализации через ViewSet"""
# class ParticipantViewSet(ViewSet):
#
#     def list(self, request):
#         participants = Participant.objects.all().filter(is_activate=True)
#         serializer = ParticipantModelSerializer(participants, many=True)
#         return Response(serializer.data)
#
#     @action(detail=False, methods=['get'])
#     def some_method(self, request):
#         return Response("Обработка какого-то метода")

""" Пример реализации через миксины"""
# class ParticipantViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, GenericViewSet):
#
#     queryset = Participant.objects.all().filter(is_activate=True)
#     serializer_class = ParticipantModelSerializer


class ParticipantLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 2

# class ParticipantModelViewSet(ModelViewSet):
class ParticipantModelViewSet(
        mixins.RetrieveModelMixin,
        mixins.UpdateModelMixin,
        mixins.ListModelMixin,
        GenericViewSet):

    queryset = Participant.objects.all().filter(is_activate=True)
    serializer_class = ParticipantModelSerializer

    # def get_queryset(self):
    #
    #     queryset = Participant.objects.all().filter(is_activate=True)
    #     pagination_class = ParticipantLimitOffsetPagination
    #
    #     # Фильтр в запросе
    #     if 'name' in self.request.query_params:
    #         # В параметрах может быть только одно значение
    #         for search_elem in self.request.query_params['name']:
    #             queryset = queryset.filter(first_name__contains=search_elem)
    #     # Фильтр в заголовке запроса
    #     if 'name' in self.request.headers:
    #         # В заголовке может быть только одно значение
    #         queryset = queryset.filter(
    #             first_name__contains=self.request.headers['name'])
    #     # Фильтр в параметры урла
    #     if self.kwargs and 'pk' in self.kwargs:
    #         # В заголовке может быть только одно значение
    #         queryset = queryset.filter(first_name__contains=self.kwargs['pk'])
    #
    #     return queryset
