from .models import (BloodBankDonor,Donor,BloodCompatibility)
from rest_framework import serializers
from datetime import datetime

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
        '''date1=data['last_donated_date']
        date2=datetime.now().date()
        diff=date1-date2'''
        '''dob=data['dob']
        diff2=date2-dob'''
    

        if weight<50 or diseases=='yes' or allergies=='yes' or cardiac=='yes' or bleeding=='yes' or hepatitis=='yes' or hiv=='yes' '''diff.days<90 or diff2.days<6570:''':
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


    class Meta:
        model=Donor
        fields='__all__'
    
    def to_representation(self,instance):
        rep= super(DonorSerializer,self).to_representation(instance)
        rep['blood_group'] = instance.blood_group.p_blood
        return rep
    

