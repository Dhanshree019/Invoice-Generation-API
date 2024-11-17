from rest_framework import serializers
from .models import Invoice, InvoiceDetail

class InvoiceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceDetail
        fields = ['id', 'description', 'quantity', 'price', 'line_total']

class InvoiceSerializer(serializers.ModelSerializer):
    details = InvoiceDetailSerializer(many=True)

    class Meta:
        model = Invoice
        fields = ['id', 'invoice_number', 'customer_name', 'date', 'details']

    def create(self, validated_data):
        try:
            details_data = validated_data.pop('details')
            invoice = Invoice.objects.create(**validated_data)
            for detail in details_data:
                InvoiceDetail.objects.create(invoice=invoice, **detail)
            return invoice
        except Exception as e:
            raise serializers.ValidationError({"error": f"Failed to create invoice: {str(e)}"})

    def update(self, instance, validated_data):
        try:
            details_data = validated_data.pop('details')
            instance.invoice_number = validated_data.get('invoice_number', instance.invoice_number)
            instance.customer_name = validated_data.get('customer_name', instance.customer_name)
            instance.date = validated_data.get('date', instance.date)
            instance.save()

            # Clear existing details
            instance.details.all().delete()

            # Add new details
            for detail in details_data:
                InvoiceDetail.objects.create(invoice=instance, **detail)
            
            return instance
        except Exception as e:
            raise serializers.ValidationError({"error": f"Failed to update invoice: {str(e)}"})
