from django.urls import path


from task_one.views.contract_unique_manufacturers import ContractUniqueManufacturersView
from task_one.views.loan_applications_list import LoanApplicationsListView

urlpatterns = [
    path('contract/<uuid:contract_id>/', ContractUniqueManufacturersView.as_view(), name='contract_unique_manifacturer'),
    path('', LoanApplicationsListView.as_view(), name='loan_applications_list'),
]
