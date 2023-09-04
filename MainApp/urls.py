from django.contrib import admin
from MainApp import views
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',  views.inicio, name='Inicio'),
    path('access-point-form', views.add_access_point, name='AddAccessPoint'),
    path('switches-form', views.add_switch, name='AddSwitch'),
    path('access-points', views.access_points, name='AccessPoints'),
    path('switches', views.switches, name='Switches'),
    path('busqueda', views.busqueda, name="Busqueda"),
    path('buscar/', views.buscar),
]
