from django.shortcuts import render
from .models import Device

def home(request):

    devices = Device.objects.all()

    return render(request, 'home.html', {
        'device_list': devices
    })
