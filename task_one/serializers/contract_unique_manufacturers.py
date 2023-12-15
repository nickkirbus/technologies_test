from typing import Dict
from rest_framework import serializers


class ContractUniqueManufacturersSerializer(serializers.Serializer):
    manufacturer_id = serializers.SerializerMethodField(read_only=True)

    def get_manufacturer_id(self, obj: Dict):
        return str(obj['manufacturer'])
