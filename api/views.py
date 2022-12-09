from django.shortcuts import render
from rest_framework import generics
from .serializers import (BloodBankDonorSerializer, BloodCompatibilitySerializer,DonorSerializer,CustomUserSerializer,DistrictSerializer)
from .models import (BloodBankDonor,Donor,BloodCompatibility,CustomAccountManager,NewUser,Districts)
from rest_framework import generics,mixins,viewsets,status
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken,AccessToken
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.permissions import AllowAny

# Create your views here

class CustomUserCreate(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format='json'):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlacklistTokenUpdateView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = ()

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

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

class DistrictsList(generics.ListAPIView):
    queryset = Districts.objects.all()
    serializer_class=DistrictSerializer    