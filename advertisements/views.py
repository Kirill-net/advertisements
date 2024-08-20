from django_filters import DateFromToRangeFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from advertisements.filters import AdvertisementFilter
from advertisements.models import Advertisement
from advertisements.permissions import IsOwner
from advertisements.serializers import AdvertisementSerializer


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров

    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwner]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter, ]
    filterset_fields = ['creator', 'status', ]
    ordering_fields = ['id', 'creator', 'created_at', ]
    filterset_class = AdvertisementFilter

