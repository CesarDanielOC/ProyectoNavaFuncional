from django.urls import path
from receta_app import views

urlpatterns = [
    path('Receta', views.inicio_vistaReceta, name="Receta"),
    path("registrarReceta/", views.registrarReceta, name="registrarReceta/"),
    path("seleccionarReceta/str:<idreceta>", views.seleccionarReceta, name="seleccionarReceta/"),
    path("editarReceta/", views.editarReceta, name="editarReceta/"),
    path("borrarReceta/str:<idreceta>", views.borrarReceta, name="borrarReceta/"),
]
