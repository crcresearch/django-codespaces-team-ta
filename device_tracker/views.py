from django.shortcuts import render
from .models import Device

def home(request):

    devices = Device.objects.filter(name__icontains='Sam')
    return render(request, 'home.html', {
        'device_list': devices
    })

def home_boostrap(request):
    return render(request, 'home_bootstrap.html', {})

