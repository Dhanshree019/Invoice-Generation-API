from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Invoice
from .serializers import InvoiceSerializer

class InvoiceAPIView(APIView):
    def post(self, request):
        try:
            serializer = InvoiceSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {"message": "Invoice created successfully", "data": serializer.data}, status=status.HTTP_201_CREATED
                )
            return Response(
                {"message": "Validation error", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            return Response(
                {"message": "Failed to create invoice", "error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def put(self, request, pk=None):
        try:
            invoice = Invoice.objects.get(pk=pk)
            serializer = InvoiceSerializer(invoice, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {"message": "Invoice updated successfully", "data": serializer.data}, status=status.HTTP_200_OK
                )
            return Response(
                {"message": "Validation error", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
            )
        except Invoice.DoesNotExist:
            return Response(
                {"message": "Invoice not found"}, status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {"message": "Failed to update invoice", "error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
