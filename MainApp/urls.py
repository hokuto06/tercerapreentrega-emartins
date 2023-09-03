from django.contrib import admin
from MainApp import views
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',  views.inicio, name='Inicio')
]
