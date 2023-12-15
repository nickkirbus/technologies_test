import uuid
from django.db import models


class Contract(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_created = models.DateTimeField(auto_now_add=True, editable=False)
    date_modified = models.DateTimeField(auto_now=True, editable=False)
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'contract'
        db_table = 'contract'

class LoanApplication(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_created = models.DateTimeField(auto_now_add=True, editable=False)
    date_modified = models.DateTimeField(auto_now=True, editable=False)
    name = models.CharField(max_length=255)
    contract = models.OneToOneField(Contract, on_delete=models.PROTECT, null=False, blank=True, related_name='%(class)s_contract_set')
    
    class Meta:
        verbose_name = 'loan_application'
        db_table = 'loan_application'

class Manufacturer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_created = models.DateTimeField(auto_now_add=True, editable=False)
    date_modified = models.DateTimeField(auto_now=True, editable=False)
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'manufacturer'
        db_table = 'manufacturer'

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_created = models.DateTimeField(auto_now_add=True, editable=False)
    date_modified = models.DateTimeField(auto_now=True, editable=False)
    name = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.PROTECT)
    loan_application = models.ForeignKey(LoanApplication, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'product'
        db_table = 'product'