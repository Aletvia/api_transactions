from rest_framework import serializers

from api.seriealizers.s_companies import SerializedCompanyName
from api.models.transaction import Transaction


class SerializedTransaction(serializers.ModelSerializer):
    company = SerializedCompanyName

    class Meta:
        model = Transaction
        fields = '__all__'