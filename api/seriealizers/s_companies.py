from api.models.company import Company
from rest_framework import serializers

class SerializedCompany(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = '__all__'
        
    def create(self, validated_data):
        """
        Create and return a new `Payable` instance, given the validated data.
        """
        return Company.objects.create(**validated_data)