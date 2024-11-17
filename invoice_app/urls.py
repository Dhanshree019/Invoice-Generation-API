from django.urls import path
from .views import InvoiceAPIView

urlpatterns = [
    path('invoices/', InvoiceAPIView.as_view(), name='invoice_create'),
    path('invoices/<int:pk>/', InvoiceAPIView.as_view(), name='invoice_update'),
]
