from django.urls import path
from medico_app import views

urlpatterns = [
    path('Medico',views.inicio_vistaMedico,name="Medico"),
    path("registrarMedico/",views.registrarMedico,name="registrarMedico"),
    path("seleccionarMedico/<idmedico>",views.seleccionarMedico,name="seleccionarMedico"),
    path("editarMedico/",views.editarMedico,name="editarMedico"),
    path("borrarMedico/<idmedico>",views.borrarMedico,name="borrarMedico")
]