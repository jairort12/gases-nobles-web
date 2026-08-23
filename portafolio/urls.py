from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('servicio/<str:url_id>/', views.detalle_servicio, name='detalle'),
]