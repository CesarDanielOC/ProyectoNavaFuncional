from django.shortcuts import render, redirect
from .models import Medicamento

# Create your views here.

def inicio_vistaMedicamento(request):
    losmedicamentos = Medicamento.objects.all()
    return render(request, 'gestionarMedicamento.html', {'mismedicamentos': losmedicamentos})

def registrarMedicamento(request):
    id_medicamento = request.POST["numidmedicamento"]
    nombre = request.POST["txtnombre"]
    descripcion = request.POST["txtdescripcion"]
    dosis = request.POST["txtdosis"]
    frecuencia = request.POST["numfrecuencia"]
    efectos = request.POST["txtefectos"]
    precio = request.POST["txtprecio"]

    Medicamento.objects.create(
        id_medicamento=id_medicamento, 
        nombre=nombre, 
        descripcion=descripcion, 
        dosis=dosis, 
        frecuencia=frecuencia, 
        efectos=efectos, 
        precio=precio
    )

    return redirect('Medicamento')

def seleccionarMedicamento(request, id_medicamento):
    try:
        medicamento = Medicamento.objects.get(id_medicamento=id_medicamento)
        return render(request, "editarMedicamento.html", {"mismedicamentos": medicamento})
    except Medicamento.DoesNotExist:
        return redirect('Medicamento')  # Redirigir si el medicamento no se encuentra

def editarMedicamento(request):
    if request.method == "POST":
        id_medicamento = request.POST.get("numidmedicamento")
        nombre = request.POST.get("txtnombre")
        descripcion = request.POST.get("txtdescripcion")
        dosis = request.POST.get("txtdosis")
        frecuencia = request.POST.get("numfrecuencia")
        efectos= request.POST.get("txtefectos")
        precio = request.POST.get("txtprecio")

        try:
            medicamento = Medicamento.objects.get(id_medicamento=id_medicamento)
            medicamento.nombre = nombre
            medicamento.descripcion = descripcion
            medicamento.dosis = dosis
            medicamento.frecuencia = frecuencia
            medicamento.efectos = efectos
            medicamento.precio = precio
            medicamento.save()
        except Medicamento.DoesNotExist:
            return redirect('Medicamento')  # O manejar el error según lo necesites

    return redirect('Medicamento')

def borrarMedicamento(request, id_medicamento):
    try:
        medicamento = Medicamento.objects.get(id_medicamento=id_medicamento)
        medicamento.delete()
    except Medicamento.DoesNotExist:
        pass 

    return redirect('Medicamento')
