from django.urls import path
from medicamento_app import views

urlpatterns = [
    path('Medicamento',views.inicio_vistaMedicamento,name="Medicamento"),
    path("registrarMedicamento/",views.registrarMedicamento,name="registrarMedicamento"),
    path("seleccionarMedicamento/<id_medicamento>",views.seleccionarMedicamento,name="seleccionarMedicamentoo"),
    path("editarMedicamento/",views.editarMedicamento,name="editarMedicamento"),
    path("borrarMedicamento/<id_medicamento>",views.borrarMedicamento,name="borrarPMedicamento")
]