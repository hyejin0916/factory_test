from rest_framework import serializers, status
from rest_framework.response import Response

from .models import Factory


class FactorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Factory
        fields = ['factory_name','factory_number','factory_address','ceo_name',
                  'business_number','business_registration_file']

        