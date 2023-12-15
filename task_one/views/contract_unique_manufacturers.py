from rest_framework import generics, filters
from rest_framework.request import Request
from rest_framework import status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from uuid import UUID
from task_one.models import Product
from task_one.serializers.contract_unique_manufacturers import ContractUniqueManufacturersSerializer
from django.db.models import Count

class ContractUniqueManufacturersView(generics.GenericAPIView):
    queryset = Product.objects.select_related('loan_application__contract', 'manufacturer').all()
    serializer_class = ContractUniqueManufacturersSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, )
    def get(self, request: Request, contract_id: UUID ):
        filter_queryset = self.get_queryset().filter(loan_application__contract__id=contract_id).values('manufacturer').annotate(manufacturer_cnt=Count('id'))
        serializer = self.get_serializer(filter_queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK) 