from .views import (DonorList,DonorCreate, DonorDetail,DonorUpdate,DonorDelete,BloodBankDonorList,LoggedInUserView,BlacklistTokenView,DistrictsList,RegisterView)
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,)
from email.mime import base

router=DefaultRouter()
router.register('register',RegisterView,basename='register')
router.register('donors-register',DonorCreate,basename='donors-register')
urlpatterns = [
    path('',include(router.urls)),
    path('donors/', DonorList.as_view()),
    path('donors/<int:pk>/', DonorDetail.as_view()),
    # path('donors/register/', DonorCreate.as_view()),
    path('donors-update/<int:pk>/', DonorUpdate.as_view()),
    path('donors-delete/<int:pk>/', DonorDelete.as_view()),
    path('blood-bank/', BloodBankDonorList.as_view()),
    path('api/token/',TokenObtainPairView.as_view(),name="token_obtain"),
    path('api/token/refresh/',TokenRefreshView.as_view(),name="refresh_token"),
    #path('create/', RegisterView.as_view(), name="create_user"),
    path('logout/blacklist/', BlacklistTokenView.as_view(),
         name='blacklist'),
    path('current-user/', LoggedInUserView.as_view(), name='currentuser'),
    path('districts/', DistrictsList.as_view()),     
]
