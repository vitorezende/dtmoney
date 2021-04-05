from django.db import models
from uuid import uuid4
# Create your models here.

class Transactions (models.Model):
  transaction_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
  transaction_title = models.CharField(max_length=255)
  transaction_type = models.CharField(max_length=255)
  transaction_category = models.CharField(max_length=255)
  transaction_amount = models.FloatField()
  transaction_createdAt = models.DateField(auto_now_add=True)