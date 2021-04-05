from rest_framework import serializers
from financeiro import models

class FinanceiroSerializer (serializers.ModelSerializer):
  class Meta:
    model = models.Transactions
    fields = '__all__'