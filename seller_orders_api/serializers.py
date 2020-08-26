from rest_framework import serializers
from .models import SellerOrders


class SellerOrdersSerializer(serializers.ModelSerializer):

    class Meta:

        model = SellerOrders
        fields = '__all__'
