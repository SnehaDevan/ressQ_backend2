from django.shortcuts import render
from rest_framework import generics
from .serializers import (BloodBankDonorSerializer, BloodCompatibilitySerializer,DonorSerializer,UserSerializer,DistrictSerializer,RegisterSerializer)
from .models import (BloodBankDonor,Donor,BloodCompatibility,UserManager,User,Districts)
from rest_framework import generics,mixins,viewsets,status
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken,AccessToken
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.permissions import AllowAny

# Create your views here

class RegisterView(viewsets.GenericViewSet,mixins.CreateModelMixin):
    serializer_class=RegisterSerializer
    queryset=User.objects.all()


class LoggedInUserView(APIView):
    permission_classes=[IsAuthenticated]
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

class BlacklistTokenView(APIView):
    permission_classes=[IsAuthenticated]
    def post(self,request):
        try:
            refresh_token=request.data["refresh_token"]
            token=RefreshToken(refresh_token)
            token.blacklist()
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

class DonorCreate(viewsets.GenericViewSet,mixins.DestroyModelMixin,mixins.UpdateModelMixin,mixins.CreateModelMixin,mixins.RetrieveModelMixin,mixins.ListModelMixin):
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