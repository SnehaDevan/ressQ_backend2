from django.db import models
from distutils.command.upload import upload
from inspect import modulesbyfile
from unittest.util import _MAX_LENGTH
from django.conf import settings
from email.policy import default
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import (AbstractBaseUser,BaseUserManager,PermissionsMixin)

# Create your models here.

class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, user_name, first_name, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, user_name, first_name, password, **other_fields)

    def create_user(self, email, user_name, first_name, password, **other_fields):

        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name,
                          first_name=first_name, **other_fields)
        user.set_password(password)
        user.save()
        return user


class NewUser(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(_('email address'), unique=True)
    user_name = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    start_date = models.DateTimeField(default=timezone.now)
    about = models.TextField(_(
        'about'), max_length=500, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'first_name']

    def __str__(self):
        return self.user_name

class Districts(models.Model):
    district_name=models.CharField(max_length=50)
    def __str__(self):
        return self.district_name

class BloodBankDonor(models.Model):
    quantity_available=models.FloatField()
    b_manager=models.CharField(max_length=100)
    contact=models.CharField(max_length=10)
    address=models.TextField(max_length=300)
    b_name=models.CharField(max_length=100)

    def __str__(self):
        return self.b_name

class BloodCompatibility(models.Model):
    p_blood=models.CharField(max_length=3)
    comp_type1=models.CharField(max_length=3,blank=True, null=True)
    comp_type2=models.CharField(max_length=3,blank=True, null=True)
    comp_type3=models.CharField(max_length=3,blank=True, null=True)
    comp_type4=models.CharField(max_length=3,blank=True, null=True)
    comp_type5=models.CharField(max_length=3,blank=True, null=True)
    comp_type6=models.CharField(max_length=3,blank=True, null=True)
    comp_type7=models.CharField(max_length=3,blank=True, null=True)
    comp_type8=models.CharField(max_length=3,blank=True, null=True)

    def __str__(self):
        return self.p_blood
        
class Donor(models.Model):
    dname = models.CharField(max_length=100)
    gender_choices=[
        ('male',"Male"),
        ("female","Female"),
        ("Others","others"),
    ]
    gender = models.CharField(
        max_length=6,choices=gender_choices,
        )
    dob = models.DateField()

    blood_group = models.ForeignKey(BloodCompatibility,on_delete=models.CASCADE)
    phoneno = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    weight = models.IntegerField()
    class_name_choices=(
        ("csa","CSA"),
        ("csb","CSB"),
        ("eca","ECA"),
        ("ecb","ECB"),
        ("eee","EEE"),
        ("mech","MECH"),
        ("eb","EB"),
    )
    class_name= models.CharField(max_length=4,choices=class_name_choices)
    batch_choices = (
        ("2023","2023"),
        ("2024","2024"),
        ("2025","2025"),
        ("2026","2026"),
    )
    batch = models.CharField(max_length=4,choices=batch_choices)
    city = models.CharField(max_length=50)
    district = models.ForeignKey(Districts,on_delete=models.CASCADE)
    pincode = models.CharField(max_length=6)
    last_donated_date = models.DateField(blank=True,null=True)
    diseases_choices = (
        ("no","No"),
        ("yes","Yes"),
    )
    diseases = models.CharField(max_length=3,choices=diseases_choices)
    allergies_choices = (
        ("no","No"),
        ("yes","Yes"),
    )
    allergies = models.CharField(max_length=3,choices=allergies_choices)
    cardiac_choices=[
        ("no", "No"),
        ("yes","Yes"),
    ]
    cardiac = models.CharField(
        max_length=4, blank=True, null=True,
        choices=cardiac_choices,
        )
    bleeding_disorders_choices=[
        ("no","No"),
        ("yes","Yes"),
    ]
    bleeding_disorders = models.CharField(
        max_length=4, blank=True, null=True,
        choices=bleeding_disorders_choices,
        )
    hiv_choices=[
        ("no","No"),
        ("yes","Yes"),
    ]
    hiv =models.CharField(
        max_length=4, blank=True, null=True,
        choices=hiv_choices,
        )
    hepatitis_choices=[
        ("no","No"),
        ("yes","Yes"),
    ]
    hepatitis =models.CharField(
        max_length=4, blank=True, null=True,
        choices=hepatitis_choices,
        )
    


    def __str__(self):
        return self.dname
