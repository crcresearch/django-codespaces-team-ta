from django.contrib import admin
from device_tracker.models import Device, DeviceType, DeviceLocation

# Register your models here.
admin.site.register(DeviceType)
admin.site.register(Device)
admin.site.register(DeviceLocation)