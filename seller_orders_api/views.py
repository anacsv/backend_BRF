from rest_framework import viewsets, permissions
from .models import SellerOrders
from seller_orders_api.serializers import SellerOrdersSerializer


# Create your views here.
class SellerOrdersApi(viewsets.ModelViewSet):

    queryset = SellerOrders.objects.all().order_by('created_at')
    serializer_class = SellerOrdersSerializer

    permission_classes = [permissions.IsAuthenticated]