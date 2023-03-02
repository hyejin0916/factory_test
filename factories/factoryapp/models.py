import os
from django.conf import settings
from django.db import models

# Create your models here.
    
class Factory(models.Model):
    factory_name = models.CharField(max_length=50, null=True, blank=True) # 공장명
    factory_number = models.CharField(max_length=11, unique=True, null=True, blank=True) # 공장 전화번호
    factory_address = models.CharField(max_length=100, null=True, blank=True) # 회사 주소
    ceo_name = models.CharField(max_length=100, null=True, blank=True) # 대표자명
    business_number = models.CharField(max_length=10, null=True, blank=True) # 사업자 번호
    business_registration_file = models.ImageField(upload_to='media', null=True, blank=True)
    # 사업자 등록 파일
    
    # Factory 데이터가 삭제되면 해당하는 이미지 파일도 함께 삭제
    def delete(self, *args, **kwargs):
        super(Factory, self).delete(*args, **kwargs)
        os.remove(os.path.join(settings.MEDIA_ROOT, self.business_registration_file.path))
    
    # admin
    def __str__(self):
        return f"ID: {self.id}, 공장명: {self.factory_name}, 대표자: {self.ceo_name}, 주소: {self.factory_address}"