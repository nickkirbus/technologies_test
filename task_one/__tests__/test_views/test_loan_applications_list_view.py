from pilot_project.settings import PAGE_SIZE
import pytest
from django.urls import reverse
from django.test import Client
pytestmark = pytest.mark.django_db

class TestLoanApplicationsListView:
    URL = 'loan_applications_list'
    def test_get(self, client: Client, create_10_loadn_applications: None):
        url = reverse(self.URL)
        response = client.get(url, content_type='application/json')
        assert response.status_code == 200
        assert len(response.data) == PAGE_SIZE
        assert response.data[0]['id']
        assert response.data[0]['contract']
        assert response.data[0]['contract']['id']
        assert response.data[0]['contract']['name']
