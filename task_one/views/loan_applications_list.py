from rest_framework import generics
from rest_framework.request import Request
from rest_framework import status
from rest_framework.response import Response
from uuid import UUID
from task_one.models import LoanApplication
from task_one.serializers.loan_applications_list import LoanApplicationsListSerializer

class LoanApplicationsListView(generics.GenericAPIView):
    queryset = LoanApplication.objects.select_related('contract').all()
    serializer_class = LoanApplicationsListSerializer
    def get(self, request: Request):
        page = self.paginate_queryset(self.get_queryset())
        serializer = self.get_serializer(page, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK) 