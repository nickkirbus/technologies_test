from task_one.models import Contract, LoanApplication, Manufacturer, Product
import pytest
pytestmark = pytest.mark.django_db

class TestProductModel:
    def test_product_model(self) -> None:
        contract = Contract.objects.create(name='test_contract')
        manufacturer = Manufacturer.objects.create(name='test_manufacturer_name')
        loan_application = LoanApplication.objects.create(contract=contract, name='test_loan')
        product = Product.objects.create(manufacturer=manufacturer, loan_application=loan_application, name='test_product_name')
        assert product.id