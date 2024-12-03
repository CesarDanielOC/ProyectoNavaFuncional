from django.contrib import admin
from django.urls import path, include
from app_base import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio,name='inicio'),
    path('Paciente/', include('paciente_app.urls')),  
    path('Medico/', include('medico_app.urls')),
    path('Citas/', include('citas_app.urls')),
    path('Medicamento/', include('medicamento_app.urls')),
    path('Receta/', include('receta_app.urls')),
]
