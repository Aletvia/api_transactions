from api.models.company import Company
from rest_framework import serializers

class SerializedCompany(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ['name', 'active']

