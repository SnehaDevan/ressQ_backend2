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

class UserManager(BaseUserManager):
    def create_user(self,username,email,password=None):
        if username is None:
            raise TypeError("Users should have a username")

        if email is None:
            raise TypeError("Users should have a email")

        user=self.model(username=username,email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,username,email,password=None):
        if password is None:
            raise TypeError("Password should not be none")
        
        # user=self.create_user(username,email,password)
        user=self.create_user(username,email,password)
        user.is_superuser=True
        user.is_staff=True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser,PermissionsMixin):
    username=models.CharField(max_length=255,unique=True,db_index=True)
    email=models.EmailField(max_length=255,unique=True,db_index=True)
    is_verified=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username']

    objects=UserManager()
    def __str__(self):
        return self.username

    def tokens(self):
        return ''


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
    user_foreign = models.ForeignKey(User, on_delete=models.CASCADE)
    dname = models.CharField(max_length=100)
    gender_choices=[
        ("Male","Male"),
        ("Female","Female"),
        ("Others","Others"),
    ]
    gender = models.CharField(
        max_length=6,choices=gender_choices,
        )
    dob = models.DateField()

    blood_group = models.CharField(max_length=5)
    phoneno = models.CharField(max_length=10)
    weight = models.IntegerField()
    branch_choices=(
        ("CSA","CSA"),
        ("CSB","CSB"),
        ("ECA","ECA"),
        ("ECB","ECB"),
        ("EEE","EEE"),
        ("MECH","MECH"),
        ("EB","EB"),
    )
    branch= models.CharField(max_length=4,choices=branch_choices)
    batch_choices = (
        ("2023","2023"),
        ("2024","2024"),
        ("2025","2025"),
        ("2026","2026"),
    )
    batch = models.CharField(max_length=4,choices=batch_choices)
    district = models.CharField(max_length=50)
    last_donated_date = models.DateField(blank=True,null=True)
    diseases_choices = (
        ("No","No"),
        ("Yes","Yes"),
    )
    diseases = models.CharField(max_length=3,choices=diseases_choices)
    allergies_choices = (
        ("No","No"),
        ("Yes","Yes"),
    )
    allergies = models.CharField(max_length=3,choices=allergies_choices)
    cardiac_choices=[
        ("No", "No"),
        ("Yes","Yes"),
    ]
    cardiac = models.CharField(
        max_length=4, blank=True, null=True,
        choices=cardiac_choices,
        )
    bleeding_disorders_choices=[
        ("No","No"),
        ("Yes","Yes"),
    ]
    bleeding_disorders = models.CharField(
        max_length=4, blank=True, null=True,
        choices=bleeding_disorders_choices,
        )
    hiv_choices=[
        ("No","No"),
        ("Yes","Yes"),
    ]
    hiv =models.CharField(
        max_length=4, blank=True, null=True,
        choices=hiv_choices,
        )
    hepatitis_choices=[
        ("No","No"),
        ("Yes","Yes"),
    ]
    hepatitis =models.CharField(
        max_length=4, blank=True, null=True,
        choices=hepatitis_choices,
        )
    


    def __str__(self):
        return self.dname
