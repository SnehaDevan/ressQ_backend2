from .views import (DonorList,DonorCreate, DonorDetail,DonorUpdate,DonorDelete,BloodBankDonorList,CustomUserCreate,BlacklistTokenUpdateView,DistrictsList)
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,)
from email.mime import base

router=DefaultRouter()
urlpatterns = [
    path('',include(router.urls)),
    path('donors/', DonorList.as_view()),
    path('donors/<int:pk>/', DonorDetail.as_view()),
    path('donors/register/', DonorCreate.as_view()),
    path('donors-update/<int:pk>/', DonorUpdate.as_view()),
    path('donors-delete/<int:pk>/', DonorDelete.as_view()),
    path('blood-bank/', BloodBankDonorList.as_view()),
    path('api/token/',TokenObtainPairView.as_view(),name="token_obtain"),
    path('api/token/refresh/',TokenRefreshView.as_view(),name="refresh_token"),
    path('create/', CustomUserCreate.as_view(), name="create_user"),
    path('logout/blacklist/', BlacklistTokenUpdateView.as_view(),
         name='blacklist'),
    path('districts/', DistrictsList.as_view()),     
]
