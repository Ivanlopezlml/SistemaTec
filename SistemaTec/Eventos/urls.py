from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('', LoginView.as_view(template_name='login.html'), name='login'),
    path('Inicio/', views.Inicio, name='Inicio'),
    path('Convocatoria/', views.ConvocatoriaView, name='ConvocatoriaView'),   
    path('Convocatoria/add_teams', views.add_teams, name='add_teams'),
]
