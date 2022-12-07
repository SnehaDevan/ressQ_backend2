from django.contrib import admin
from .models import (BloodBankDonor,Donor,BloodCompatibility)

# Register your models here.
admin.site.register(BloodBankDonor)
admin.site.register(Donor)
admin.site.register(BloodCompatibility)
