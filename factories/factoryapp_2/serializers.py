from rest_framework import serializers
from .models import SecondFactory,SecondFactoryImage

class SecondFactoryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecondFactoryImage
        fields = ['second_business_registration_file']
        
class SecondFactorySerializer(serializers.ModelSerializer):
    second_business_registration_file = SecondFactoryImageSerializer(many=True, read_only=True)
    
    class Meta:
        model = SecondFactory
        fields = ['second_factory_name','second_factory_number','second_factory_address','second_ceo_name',
                  'second_business_number','second_business_registration_file']
        
    def create(self, validated_data):
        images_data = self.context['request'].FILES
        second_factory = SecondFactory.objects.create(**validated_data)
        for image_data in images_data.getlist('second_business_registration_file'):
            SecondFactoryImage.objects.create(second_factory=second_factory, second_business_registration_file=image_data)
        return second_factory