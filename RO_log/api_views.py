from django.db.models import query
from rest_framework.generics import ListAPIView
from RO_log.serializers import ROSerializer,PayPeriodSerializer
from RO_log.models import RO,PayPeriod

class PayPeriodList(ListAPIView):
    queryset = PayPeriod.objects.all()
    serializer_class = PayPeriodSerializer


class ROList(ListAPIView):
    queryset = RO.objects.all()
    serializer_class = ROSerializer