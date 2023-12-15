from django.core.management.base import BaseCommand

from task_one.models import Contract, LoanApplication, Manufacturer, Product


class Command(BaseCommand):
    help = 'Description of my custom command'

    def handle(self, *args, **options):

        contract = Contract.objects.create(name='test_contract')

        first_manufacturer_manufacturer = Manufacturer.objects.create(name='test_manufacturer_name')
        second_manufacturer_manufacturer = Manufacturer.objects.create(name='test_manufacturer_name_second')

        loan_application = LoanApplication.objects.create(contract=contract, name='test_loan')

        products_loan_application_one = []

        for i in range(1, 6):
            if i % 2 == 0:
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

        self.stdout.write('My custom command executed successfully')
