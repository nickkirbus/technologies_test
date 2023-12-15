import pytest
from django.urls import reverse
from django.test import Client
from task_one.models import Contract, Manufacturer
pytestmark = pytest.mark.django_db

class TestContractUniqueManufacturersView:
    URL = 'contract_unique_manifacturer'
    def test_get(self, client: Client, seed_db: None, get_contract: Contract):
        url = f"{reverse(self.URL, kwargs={'contract_id': get_contract.id})}"
        response = client.get(url, content_type='application/json')
        assert response.status_code == 200
        assert len(response.data) == Manufacturer.objects.all().count()
        assert response.data[0]['manufacturer_id'] 
        assert Manufacturer.objects.filter(id=response.data[0]['manufacturer_id']).exists()
        assert response.data[1]['manufacturer_id']
        assert Manufacturer.objects.filter(id=response.data[1]['manufacturer_id']).exists()