from django.shortcuts import render, redirect
from .models import Medico

# Create your views here.

def inicio_vistaMedico(request):
    losmedicos=Medico.objects.all()
    return render(request,'gestionarMedico.html',{'mismedicos':losmedicos})

def registrarMedico(request):
    idmedico=request.POST["txtidmedico"]
    nombre=request.POST["txtnombre"]
    apellido=request.POST["txtapellido"]
    especialidad=request.POST["txtespecialidad"]
    telefono=request.POST["txttelefono"]
    correo=request.POST["txtcorreo"]
    fechadecontratacion=request.POST["txtfechac"]


    guardarproveedor=Medico.objects.create(idmedico=idmedico,nombre=nombre,apellido=apellido,especialidad=especialidad,telefono=telefono,correo=correo,fechadecontratacion=fechadecontratacion)

    return redirect('Medico')

def seleccionarMedico(request,idmedico):
    medicos=Medico.objects.get(idmedico=idmedico)
    return render(request,"editarMedico.html",{"mismedicos":medicos})

def editarMedico(request):
    idmedico=request.POST["txtidmedico"]
    nombre=request.POST["txtnombre"]
    apellido=request.POST["txtapellido"] 
    especialidad=request.POST["txtespecialidad"]
    telefono=request.POST["txttelefono"]
    correo=request.POST["txtcorreo"]
    fechadecontratacion=request.POST["txtfechac"]


    medicos=Medico.objects.get(idmedico=idmedico)

    medicos.nombre=nombre
    medicos.apellido=apellido
    medicos.especialidad=especialidad
    medicos.telefono=telefono
    medicos.correo=correo
    medicos.fechadecontratacion=fechadecontratacion
    medicos.save()

    return redirect('Medico')

def borrarMedico(request,idmedico):
    medicos=Medico.objects.get(idmedico=idmedico)
    medicos.delete()

    return redirect('Medico')