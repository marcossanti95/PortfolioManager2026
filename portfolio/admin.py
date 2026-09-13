from django.contrib import admin
from .models import Perfil, Cartera, ActivoRentaVariable, ActivoRentaFija


@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ("usuario", "email")


@admin.register(Cartera)
class CarteraAdmin(admin.ModelAdmin):
    list_display = ("nombre", "propietario", "fecha_creacion", "valor_total")


@admin.register(ActivoRentaVariable)
class ActivoRentaVariableAdmin(admin.ModelAdmin):
    list_display = ("ticker", "cartera", "cantidad", "precio", "moneda", "calcular_valor")


@admin.register(ActivoRentaFija)
class ActivoRentaFijaAdmin(admin.ModelAdmin):
    list_display = ("ticker", "cartera", "cantidad", "precio", "moneda", "calcular_valor")