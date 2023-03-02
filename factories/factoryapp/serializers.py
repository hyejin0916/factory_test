from rest_framework import serializers, status
from rest_framework.response import Response

from .models import Factory


class FactorySerializer(serializers.ModelSerializer):
    # def update(self, instance, validated_data):
    #     print(validated_data.get('business_registration_file'))
    #     try:
    #         instance.factory_name = validated_data.get("factory_name", instance.factory_name)
    #         instance.factory_number = validated_data.get("factory_number", instance.factory_number)
    #         instance.factory_address = validated_data.get("factory_address", instance.factory_address)
    #         instance.ceo_name = validated_data.get("ceo_name", instance.ceo_name)
    #         instance.business_number = validated_data.get("business_number", instance.business_number)
    #         instance.business_registration_file = validated_data.get("business_registration_file", instance.business_registration_file)
    #         return instance
    #     except Exception as e:
    #         print(e)
    #         return Response({'result': False}, status=status.HTTP_400_BAD_REQUEST)
    class Meta:
        model = Factory
        fields = ['factory_name','factory_number','factory_address','ceo_name',
                  'business_number','business_registration_file']

        