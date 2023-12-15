
import pytest
from task_one.models import Contract, Manufacturer, LoanApplication, Product

TEST_FIRST_MANUFACTURER_NAME = 'test_manufacturer_name'
TEST_SECOND_MANUFACTURER_NAME = 'test_manufacturer_name_second'

@pytest.fixture()
def seed_db() -> None:

    contract = Contract.objects.create(name='test_contract')
    
    first_manufacturer_manufacturer = Manufacturer.objects.create(name=TEST_FIRST_MANUFACTURER_NAME)
    second_manufacturer_manufacturer = Manufacturer.objects.create(name=TEST_SECOND_MANUFACTURER_NAME)

    loan_application = LoanApplication.objects.create(contract=contract, name='test_loan')
    
    products_loan_application_one = []
    
    for i in range(1,6):
        if i%2 == 0:
            products_loan_application_one.append(
                Product(
                    manufacturer=first_manufacturer_manufacturer,
                    loan_application=loan_application,
                    name=f"test_product_name_{i}"
                )
            )
        else:
            products_loan_application_one.append(
                Product(
                    manufacturer=second_manufacturer_manufacturer,
                    loan_application=loan_application,
                    name=f"test_product_name_{i}"
                )
            )
    Product.objects.bulk_create(products_loan_application_one)

@pytest.fixture()
def get_contract(seed_db: None) -> Contract:
    return Contract.objects.first()

@pytest.fixture()
def create_10_loadn_applications() -> None:
    contract_list: list = []
    loan_applications_list: list = []
    for i in range(0,11):
        contract_list.append(Contract(name=f'test_contract_{i}'))
    Contract.objects.bulk_create(contract_list)
    contracts = Contract.objects.all()
    for i in range(0,11):
        loan_applications_list.append(LoanApplication(contract=contracts[i], name=f'test_loan_{i}'))
    LoanApplication.objects.bulk_create(loan_applications_list)