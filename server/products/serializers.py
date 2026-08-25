from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    # Keep the existing React contract: the frontend uses product._id.
    _id = serializers.IntegerField(source="id", read_only=True)

    class Meta:
        model = Product
        fields = ["_id", "name", "description", "price", "category", "stock", "image"]
