from decimal import Decimal

from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def validate_price(self, price: Decimal) -> Decimal:
        if price <= 0:
            raise serializers.ValidationError('Price must be positive')
        return price

    def validate_name(self, name: str) -> str:
        if not name.strip():
            raise serializers.ValidationError('Name cannot be empty')
        return name
