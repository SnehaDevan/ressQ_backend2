from django.urls import path
from .views import (DonorList,DonorCreate, DonorDetail,DonorUpdate,DonorDelete,BloodBankDonorList)

urlpatterns = [
    path('donors/', DonorList.as_view()),
    path('donors/<int:pk>/', DonorDetail.as_view()),
    path('donors/register/', DonorCreate.as_view()),
    path('donors-update/<int:pk>/', DonorUpdate.as_view()),
    path('donors-delete/<int:pk>/', DonorDelete.as_view()),
    path('blood-bank/', BloodBankDonorList.as_view())

]
