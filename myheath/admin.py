from django.contrib import admin

from .models import Doctor, Patient,CustomUser

admin.site.register(CustomUser)
# Register your models here.
admin.site.register(Doctor)
admin.site.register(Patient)