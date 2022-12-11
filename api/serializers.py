from django.db import models
from .models import (BloodBankDonor,Donor,BloodCompatibility,UserManager,User,Districts)
from rest_framework import serializers
from datetime import datetime
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import (RefreshToken,TokenError)
from dataclasses import field, fields
from importlib.metadata import files

class RegisterSerializer(serializers.ModelSerializer):
    password=serializers.CharField(max_length=68,min_length=6,write_only=True)

    permission_classes=[IsAuthenticated]
    class Meta:
        model=User
        fields=['email','username','password']

    def validate(self,attrs):
        email=attrs.get('email','')
        username=attrs.get('username','')

        if not username.isalnum():
            raise serializers.ValidationError("username should contain only alpha numeric chars")
        return attrs

    def create(self,validated_data):
        return User.objects.create_user(**validated_data)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username']
        
class BloodBankDonorSerializer(serializers.ModelSerializer):
    class Meta:
        model=BloodBankDonor
        fields='__all__'

class BloodCompatibilitySerializer(serializers.ModelSerializer):
    class Meta:
        model=BloodCompatibility
        fields=('p_blood')

class DonorSerializer(serializers.ModelSerializer):

    # def validate(self,data):
    #     weight=data['weight']
    #     diseases=data['diseases']
    #     allergies=data['allergies']
    #     cardiac=data['cardiac']
    #     bleeding=data['bleeding_disorders']
    #     hepatitis=data['hepatitis']
    #     hiv=data['hiv']
    #     date1=data['last_donated_date']
    #     date2=datetime.now().date()
    #     diff=date2-date1
    #     dob=data['dob']
    #     diff2=date2-dob
        
    

    #     # if weight<50 or diseases=='yes' or allergies=='yes' or cardiac=='yes' or bleeding=='yes' or hepatitis=='yes' or hiv=='yes' or diff.days<90 or diff2.days<6570 : 
    #         # raise serializers.ValidationError('Not eligible for donation.')

        

    #     return data

    # blood_group = serializers.StringRelatedField()

  
    class Meta:
        model=Donor
        fields='__all__'
    
    
   
    # def to_representation(self,instance):
    #     rep= super(DonorSerializer,self).to_representation(instance)
    #     rep['district'] = instance.district.district_name
    #     return rep

class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model=Districts
        fields='__all__'
