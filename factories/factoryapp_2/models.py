import os
from django.conf import settings
from django.db import models

# Create your models here.
    
class SecondFactory(models.Model):
    second_factory_name = models.CharField(max_length=50, null=True, blank=True) # 공장명
    second_factory_number = models.CharField(max_length=11, unique=True, null=True, blank=True) # 공장 전화번호
    second_factory_address = models.CharField(max_length=100, null=True, blank=True) # 회사 주소
    second_ceo_name = models.CharField(max_length=100, null=True, blank=True) # 대표자명
    second_business_number = models.CharField(max_length=10, null=True, blank=True) # 사업자 번호

    
    # admin
    def __str__(self):
        return f"ID: {self.id}, 공장명: {self.second_factory_name}, 대표자: {self.second_ceo_name}, 주소: {self.second_factory_address}"
    
    
class SecondFactoryImage(models.Model):
    second_factory = models.ForeignKey(SecondFactory, on_delete=models.CASCADE)
    second_business_registration_file = models.ImageField(upload_to='media2', null=True, blank=True)
    # 사업자 등록 파일