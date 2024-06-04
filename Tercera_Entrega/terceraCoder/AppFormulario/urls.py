from django.urls import path
from AppFormulario import views


urlpatterns = [
    path('',views.inicio,name="inicio"),
    path('principiante/',views.principiante,name="principiante"),
    path('intermedio/',views.intermedio,name="intermedio"),
    path('avanzado/',views.avanzado,name="avanzado"),
    path('profesional/',views.profesional,name="profesional"),
    #url de la busqueda de alumnos principiantes
    path('busquedaPrincipiante/',views.busquedaPrincipiante,name="busquedaPrincipiante"),
    path('buscar/',views.buscar, name='buscarPrincipiante'),

]