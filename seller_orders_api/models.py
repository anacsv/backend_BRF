import uuid
from django.db import models
from django.contrib.postgres.search import SearchVectorField


class SellerOrders(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    code = models.TextField(max_length=16)
    order_id = models.UUIDField()
    channel_slug = models.TextField(max_length=16)
    channel_store = models.TextField(max_length=100)
    seller_id = models.UUIDField()
    seller_name = models.TextField(max_length=100)
    purchase_timestamp = models.DateTimeField()
    status = models.TextField(max_length=20)
    approved_at = models.DateTimeField()
    shipping_limit_date = models.DateTimeField()
    availability_days = models.IntegerField()
    invoice_url = models.TextField(max_length=200)
    invoice_issue_date = models.DateTimeField()
    invoice_key = models.TextField(max_length=100)
    invoice_number = models.IntegerField()
    invoice_serial_number = models.IntegerField()
    customer_id = models.UUIDField()
    shipment_id = models.UUIDField()
    invoice_source = models.TextField(max_length=32)
    delivered_customer_date = models.DateTimeField()
    seller_brand = models.TextField(max_length=256)
    seller_email = models.TextField(max_length=254)
    invoice_danfe_url = models.TextField(max_length=200, null=True)
    cancelation_reason = models.TextField(max_length=64, null=True)
    cancelation_status = models.TextField(max_length=64, null=True)
    suspension_reason = models.TextField(max_length=64)
    estimated_delivery_date = models.DateField()
    invoice_status = models.TextField(max_length=16)
    invoice_id = models.UUIDField()
    branded_store_slug = models.TextField(max_length=32)
    search_vector = SearchVectorField()
    shipping_quote_group_id = models.UUIDField()
    payer_id = models.UUIDField()
    display_status = models.TextField(max_length=20)
    estimated_delivery_shift = models.TextField(max_length=16)
    invoice_errors = models.JSONField()


