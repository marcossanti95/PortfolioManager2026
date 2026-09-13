from django.urls import path
from . import views

urlpatterns = [
    path("registro/", views.registro, name="registro"),
    path("", views.dashboard, name="dashboard"),
    path("cartera/nueva/", views.crear_cartera, name="crear_cartera"),
    path("cartera/<int:cartera_id>/", views.detalle_cartera, name="detalle_cartera"),
    path("cartera/<int:cartera_id>/agregar/<str:tipo>/", views.agregar_activo, name="agregar_activo"),
]