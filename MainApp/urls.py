from django.contrib import admin
from MainApp import views
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',  views.inicio, name='Inicio'),
    path('access-point-form', views.add_access_point, name='AddAccessPoint'),
    path('access-points', views.access_points, name='AccessPoints'),
    path('switches', views.switches, name='Switches'),
]
