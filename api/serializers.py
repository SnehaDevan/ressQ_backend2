from django.db import models
from .models import (BloodBankDonor,Donor,BloodCompatibility,CustomAccountManager,NewUser,Districts)
from rest_framework import serializers
from datetime import datetime
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import (RefreshToken,TokenError)
from dataclasses import field, fields
from importlib.metadata import files

class CustomUserSerializer(serializers.ModelSerializer):
    """
    Currently unused in preference of the below.
    """
    email = serializers.EmailField(required=True)
    user_name = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = NewUser
        fields = ('email', 'user_name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        # as long as the fields are the same, we can just use this
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class BloodBankDonorSerializer(serializers.ModelSerializer):
    class Meta:
        model=BloodBankDonor
        fields='__all__'

class BloodCompatibilitySerializer(serializers.ModelSerializer):
    class Meta:
        model=BloodCompatibility
        fields=('p_blood')

class DonorSerializer(serializers.ModelSerializer):

    def validate(self,data):
        weight=data['weight']
        diseases=data['diseases']
        allergies=data['allergies']
        cardiac=data['cardiac']
        bleeding=data['bleeding_disorders']
        hepatitis=data['hepatitis']
        hiv=data['hiv']
        date1=data['last_donated_date']
        date2=datetime.now().date()
        diff=date2-date1
        dob=data['dob']
        diff2=date2-dob
        
    

        if weight<50 or diseases=='yes' or allergies=='yes' or cardiac=='yes' or bleeding=='yes' or hepatitis=='yes' or hiv=='yes' or diff.days<90 or diff2.days<6570 : 
            raise serializers.ValidationError('Not eligible for donation.')

        '''diseases=data['diseases']
        if diseases=='yes':
            raise serializers.ValidationError('Not eligible for donation.')

        allergies=data['allergies']
        if allergies=='yes':
            raise serializers.ValidationError('Not eligible for donation.')

        cardiac=data['cardiac']
        if cardiac=='yes':
            raise serializers.ValidationError('Not eligible for donation.')

        bleeding=data['bleeding_disorders']
        if bleeding=='yes':
            raise serializers.ValidationError('Not eligible for donation.')

        hepatitis=data['hepatitis']
        if hepatitis=='yes':
            raise serializers.ValidationError('Not eligible for donation.')

        hiv=data['hiv']
        if hiv=='yes':
            raise serializers.ValidationError('Not eligible for donation.')'''

        return data

    blood_group = serializers.StringRelatedField()

    '''district = serializers.CharField(source='district.district_name')'''
    '''blood_group = serializers.CharField(source='blood_group.p_blood')'''
    class Meta:
        model=Donor
        fields='__all__'
    
    
   
    def to_representation(self,instance):
        rep= super(DonorSerializer,self).to_representation(instance)
        rep['district'] = instance.district.district_name
        return rep

class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model=Districts
        fields='__all__'
