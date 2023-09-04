from django.shortcuts import render
#from django.http import HttpResponse
from .models import *
from .forms import *

def inicio(req):
    return render(req, 'inicio.html')

def add_access_point(req):
    if req.method == 'POST':
        myForm = AccessPointForm(req.POST)
        print(myForm)
        if myForm.is_valid:

            data = myForm.cleaned_data

            accessPoint = AccessPoints( deviceName = data['deviceName'], ipAddress = data['ipAddress'], status = data['status'])

            accessPoint.save()
            access_points = AccessPoints.objects.all()
            return render(req, "accesspoints.html", {"accessPoints": access_points})

    else:

        myForm = AccessPointForm()

    return render(req, "AccessPointForm.html", {"myForm": myForm})
   
def access_points(req):
    access_points = AccessPoints.objects.all()
    return render(req, "accesspoints.html", {"accessPoints": access_points})  

def switches(req):
    return render(req, 'switches.html')  