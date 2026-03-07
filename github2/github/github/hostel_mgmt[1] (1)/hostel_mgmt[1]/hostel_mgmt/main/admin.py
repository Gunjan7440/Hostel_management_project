from django.contrib import admin
from .models import Complaint, LeaveRequest, Profile

admin.site.register(Complaint)
admin.site.register(LeaveRequest)
admin.site.register(Profile)

# Register your models here.
