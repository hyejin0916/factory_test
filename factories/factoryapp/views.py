import json
import os
from django.conf import settings
from django.shortcuts import render
from . import serializers
from .serializers import FactorySerializer
from .models import Factory

from drf_yasg.utils import swagger_auto_schema
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

# 공장 pk를 필요로 하지않는 작업
class FactoryAPIView(APIView):
    permissions_classes = (AllowAny,)
    parser_classes = (MultiPartParser,)
    
    # 공장리스트 조회
    @swagger_auto_schema(
        operation_id="공장 리스트 조회",
        operation_description="저장되어있는 공장의 정보를 모두 출력합니다."
    )
    def get(self, request):
        try:
            factory_info = Factory.objects.all()
            factories_serializer = serializers.FactorySerializer(factory_info, many=True)
            return Response(factories_serializer.data, status=status.HTTP_200_OK)
        
        except Exception as e:
            print(e)
            return Response({'result': False}, status=status.HTTP_400_BAD_REQUEST)
    
    # 공장 데이터 추가
    @swagger_auto_schema(
        operation_id="공장 데이터 추가",
        operation_description="공장 데이터를 추가합니다.",
        request_body=serializers.FactorySerializer
    )
    def post(self, request):
        try:
            factory_serializer = serializers.FactorySerializer(data=request.data)
            if factory_serializer.is_valid():
                factory_serializer.save()
                return Response(factory_serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response({'result': False}, status=status.HTTP_400_BAD_REQUEST)
            
        except Exception as e:
            print(e)
            return Response({'result': False}, status=status.HTTP_400_BAD_REQUEST)
        

# 공장 pk를 필요로 하는 작업
class FactorySelectAPIView(APIView):
    permissions_classes = (AllowAny,)
    parser_classes = (MultiPartParser,)
    
    # 공장 object
    def get_factory_object(self, pk):
        try:
            factory_info = Factory.objects.get(id=pk)
            return factory_info
        except:
            return Response({'result': False}, status=status.HTTP_400_BAD_REQUEST)
        
    # 공장 데이터 삭제
    @swagger_auto_schema(
        operation_id="공장 데이터 삭제",
        operation_description="선택된 공장의 정보를 삭제합니다."
    )
    def delete(self, request, pk):
        try:
            factory_info = self.get_factory_object(pk=pk)
            factory_info.delete()
            return Response({'result': True}, status=status.HTTP_200_OK)
        
        except Exception as e:
            print(e)
            return Response({'result': False}, status=status.HTTP_400_BAD_REQUEST)
        
    # 특정 공장 조회
    @swagger_auto_schema(
        operation_id="특정 공장 조회",
        operation_description="선택된 공장의 정보를 보여줍니다."
    )
    def get(self, request, pk):
        try:
            factory_info = self.get_factory_object(pk=pk)
            factory_serializer = serializers.FactorySerializer(factory_info)
            print(factory_serializer.data)
            return Response(factory_serializer.data, status=status.HTTP_200_OK)
        
        except Exception as e:
            print(e)
            return Response({'result': False}, status=status.HTTP_400_BAD_REQUEST)
    
    # 공장 데이터 수정
    @swagger_auto_schema(
        operation_id="공장 데이터 수정",
        operation_description="공장 데이터를 수정합니다.",
        request_body=serializers.FactorySerializer
    )
    def patch(self, request, pk):
        try:
            factory_info = self.get_factory_object(pk=pk)
            
            # 수정할 데이터에 이미지 파일이 존재하는 경우 + 기존 데이터에 이미지 파일이 존재하는 경우 = 기존 파일을 삭제
            if request.FILES.get("business_registration_file") and factory_info.business_registration_file:
                os.remove(os.path.join(settings.MEDIA_ROOT, factory_info.business_registration_file.path))
            
            factory_serializer = serializers.FactorySerializer(instance=factory_info, data=request.data)
            
            if factory_serializer.is_valid():
                factory_serializer.save()
                return Response({'result': True}, status=status.HTTP_200_OK)
            else:
                return Response({'result': False}, status=status.HTTP_400_BAD_REQUEST)
            
        except Exception as e:
            print(e)
            return Response({'result': False}, status=status.HTTP_400_BAD_REQUEST)
        
        
        
        
        
        
        
        
    # def post(self, request, pk):
    #     try:
    #         factory_info=self.get_factory_object(pk=pk)
    #         print("factory_info",factory_info)
    #         Querydict = request.data
    #         factory_list_column = {"factory_name":None,'factory_number':None,'factory_address':None,'ceo_name':None,'business_number':None,'business_registration_file':None}
         
    #         for query in Querydict:
    #             factory_list_column[query]=Querydict[query]
    #         print(factory_list_column)
    #         # {'factory_name': None, 'factory_number': '22222', 'factory_address': '22222', 'ceo_name': None, 
    #         # 'business_number': '22222', 'business_registration_file': <InMemoryUploadedFile: 사업자 등록 파일.png (image/png)>}
                
    #         serializer = serializers.FactorySerializer()
    #         factory_serializer = serializer.factory_data_update(instance=factory_info, data=factory_list_column)
    #         print(factory_serializer.data)
    #         if factory_serializer.is_valid():
    #             factory_serializer.save()
    #             return Response({'result':True}, status=status.HTTP_200_OK)
    #         else:
    #             return Response({'result':False}, status=status.HTTP_400_BAD_REQUEST)
    #     except Exception as e:
    #         print(e)
    #         return Response({'result':False}, status=status.HTTP_400_BAD_REQUEST)