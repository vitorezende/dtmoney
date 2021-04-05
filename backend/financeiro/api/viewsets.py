from rest_framework import viewsets
from financeiro.api import serializers
from financeiro import models

class FinanceiroViewSet(viewsets.ModelViewSet):
  serializer_class = serializers.FinanceiroSerializer
  queryset = models.Transactions.objects.all()