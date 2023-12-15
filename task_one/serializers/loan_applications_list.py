from rest_framework import serializers
from task_one.models import Contract, LoanApplication


class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = ['id', 'name']


class LoanApplicationsListSerializer(serializers.ModelSerializer):
    contract = ContractSerializer()

    class Meta:
        model = LoanApplication
        fields = ['id', 'contract']
