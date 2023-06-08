from django.db import models

class DeviceType(models.Model):
    name = models.CharField(max_length=1024)
    model = models.CharField(max_length=1024)

    def __str__(self) -> str:
        return self.name + ' ' + self.model

class Device(models.Model):
    name = models.CharField(max_length=1024)
    description = models.TextField(null=True)
    device_type = models.ForeignKey(DeviceType, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.name

class DeviceLocation(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name='locations')
    latitude = models.FloatField()
    longitude = models.FloatField()
    timestamp = models.DateTimeField()

    def __str__(self) -> str:
        return f"{str(self.device)} on {self.timestamp}: [{self.latitude}, {self.longitude}]"