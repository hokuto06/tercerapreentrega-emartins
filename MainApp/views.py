from django.shortcuts import render
from django.http import HttpResponse
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

def add_switch(req):

    if req.method == 'POST':
        myForm = SwitchForm(req.POST)
        print(myForm)
        if myForm.is_valid:

            data = myForm.cleaned_data

            switches = Switches( deviceName = data['deviceName'], ipAddress = data['ipAddress'], marca = data['marca'], status = data['status'])

            switches.save()
            _switches = Switches.objects.all()
            return render(req, "switches.html", {"switches": _switches})

    else:

        myForm = SwitchForm()

    return render(req, "SwitchesForm.html", {"myForm": myForm})

def access_points(req):

    all_access_points = AccessPoints.objects.all()
    print(access_points)
    return render(req, "accesspoints.html", {"accessPoints": all_access_points})  

def switches(req):

    all_switches = Switches.objects.all()
    return render(req, 'switches.html', {"switches": all_switches}) 

def busqueda(req):

    return render(req, "search.html")

def buscar(req):

    if req.GET["ipAddress"]:
        #rsta = f"Estoy busdcando el Access Point con ip: {req.GET['ipAddress'] }"
        ipAddress = req.GET['ipAddress']
        deviceName = AccessPoints.objects.filter(ipAddress__icontains=ipAddress)
        status = AccessPoints.objects.filter(ipAddress__icontains=ipAddress)
        return render(req, "resultadosBusqueda.html", {"deviceName":deviceName, "ipAddress":ipAddress, "status":status})
        #return HttpResponse(rsta)
    
    else:
        rsta = "No se ingresaron datos"
    
    return HttpResponse(rsta)

def servers(req):

    all_servers = Servers.objects.all()
    return render(req, 'servers.html', {"servers": all_servers}) 

def add_server(req):

    if req.method == 'POST':
        myForm = ServerForm(req.POST)
        print(myForm)
        if myForm.is_valid:

            data = myForm.cleaned_data

            servers = Servers( deviceName = data['deviceName'], ipAddress = data['ipAddress'], service = data['service'], status = data['status'])

            servers.save()
            _servers = Servers.objects.all()
            return render(req, "servers.html", {"servers": _servers})
    else:
        myForm = ServerForm()
    return render(req, "AccessPointForm.html", {"myForm": myForm})