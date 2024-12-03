from django.shortcuts import render, redirect
from .models import Citas

# Create your views here.

def inicio_vistaCitas(request):
    lascitas=Citas.objects.all()
    return render(request,'gestionarCitas.html',{'miscitas':lascitas})

def registrarCitas(request):
    idcita=request.POST["txtidcitas"]
    idpaciente=request.POST["txtidpaciente"]
    idmedico=request.POST["txtidmedico"]
    fechacita=request.POST["txtfechacita"]
    horacita=request.POST["txthoracita"]
    motivo=request.POST["txtmotivo"]
    estado=request.POST["txtestado"]

    guardarcitas=Citas.objects.create(idcita=idcita,idpaciente=idpaciente,idmedico=idmedico,fechacita=fechacita,horacita=horacita,motivo=motivo,estado=estado)

    return redirect('Citas')

def seleccionarCitas(request,idcita):
    citas=Citas.objects.get(idcita=idcita)
    return render(request,"editarCitas.html",{"miscitas":citas})

def editarCitas(request):
    idcita=request.POST["txtidcitas"]
    idpaciente=request.POST["txtidpaciente"]
    idmedico=request.POST["txtidmedico"] 
    fechacita=request.POST["txtfechacita"]
    horacita=request.POST["txthoracita"]
    motivo=request.POST["txtmotivo"]
    estado=request.POST["txtestado"]

    citas=Citas.objects.get(idcita=idcita)

    citas.idpaciente=idpaciente
    citas.idmedico=idmedico
    citas.fechacita=fechacita
    citas.horacita=horacita
    citas.motivo=motivo
    citas.estado=estado
    citas.save()

    return redirect('Citas')

def borrarCitas(request,idcita):
    citas=Citas.objects.get(idcita=idcita)
    citas.delete()

    return redirect('Citas')