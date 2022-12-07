from django.db import models

# Create your models here.

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
    district = models.CharField(max_length=50)
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
