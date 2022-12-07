from django.shortcuts import render
from rest_framework import generics
from .serializers import (BloodBankDonorSerializer, BloodCompatibilitySerializer,DonorSerializer)
from .models import (BloodBankDonor,Donor,BloodCompatibility)


# Create your views here

class DonorList(generics.ListAPIView):
    serializer_class= DonorSerializer

    def get_queryset(self):
        queryset= Donor.objects.all()
        bg = self.request.query_params.get('bg')
        if bg is not None:
            queryset= queryset.filter(blood_group=bg)
        return queryset

class DonorCreate(generics.CreateAPIView):
    queryset = Donor.objects.all()
    serializer_class=DonorSerializer

class DonorDetail(generics.RetrieveAPIView):
    queryset =Donor.objects.all()
    serializer_class = DonorSerializer

class DonorUpdate(generics.RetrieveUpdateAPIView):
    queryset = Donor.objects.all()
    serializer_class = DonorSerializer

class DonorDelete(generics.RetrieveDestroyAPIView):
    queryset = Donor.objects.all()
    serializer_class = DonorSerializer
    
class BloodBankDonorList(generics.ListAPIView):
    queryset = BloodBankDonor.objects.all()
    serializer_class=DonorSerializer