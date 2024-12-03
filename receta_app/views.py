from django.shortcuts import render, redirect
from .models import Receta

def inicio_vistaReceta(request):
    lasrecetas = Receta.objects.all()
    return render(request, 'gestionarReceta.html', {'misrecetas': lasrecetas})

def registrarReceta(request):
    idreceta = request.POST["txtidreceta"]
    idpaciente = request.POST["txtidpaciente"]
    idmedico = request.POST["txtidmedico"]
    fechareceta = request.POST["txtfechareceta"]
    instrucciones = request.POST["txtinstrucciones"]
    validez = request.POST["txtvalidez"]
    idmedicamento = request.POST["txtidmedicamento"]

    guardarpedido = Receta.objects.create(idreceta=idreceta, idpaciente=idpaciente, idmedico=idmedico,fechareceta=fechareceta, instrucciones=instrucciones,validez=validez, idmedicamento=idmedicamento)

    return redirect('Receta')

def seleccionarReceta(request, idreceta):
    Receta_ = Receta.objects.get(idreceta=idreceta)
    return render(request, "editarReceta.html", {"mirecetas": Receta_})

def editarReceta(request):
    idreceta = request.POST.get("txtidreceta")
    idpaciente = request.POST.get("txtidpaciente")
    idmedico = request.POST.get("txtidmedico")
    fechareceta = request.POST.get("txtfechareceta")
    instrucciones = request.POST.get("txtinstrucciones")
    validez = request.POST.get("txtvalidez")
    idmedicamento = request.POST.get("txtidmedicamento")

    Receta_ = Receta.objects.get(idreceta=idreceta)

    Receta_.idpaciente = idpaciente
    Receta_.idmedico = idmedico
    Receta_.fechareceta = fechareceta
    Receta_.instrucciones = instrucciones
    Receta_.validez = validez
    Receta_.idmedicamento = idmedicamento
    Receta_.save()

    return redirect('Receta')

def borrarReceta(request, idreceta):
    Receta_ = Receta.objects.get(idreceta=idreceta)
    Receta_.delete()

    return redirect('Receta')
