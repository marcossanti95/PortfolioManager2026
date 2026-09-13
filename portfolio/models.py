from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator


MONEDA_CHOICES = [
    ("ARS", "Pesos argentinos"),
    ("USD", "Dólares estadounidenses"),
]


class Perfil(models.Model):
    """
    Extiende al User de Django. Cumple el requisito de 'registro y perfiles'
    y reemplaza conceptualmente a la clase Cliente del proyecto de POO.
    """
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(blank=True)

    def __str__(self):
        return f"Perfil de {self.usuario.username}"


class Cartera(models.Model):
    """
    Equivalente a la clase Cartera del proyecto de POO.
    Cada cartera pertenece a un Perfil (relación de asociación/propiedad).
    """
    propietario = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name="carteras")
    nombre = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def valor_total(self):
        total = 0
        for activo in self.activorentavariable_set.all():
            total += activo.calcular_valor()
        for activo in self.activorentafija_set.all():
            total += activo.calcular_valor()
        return total

    def todos_los_activos(self):
        return list(self.activorentavariable_set.all()) + list(self.activorentafija_set.all())

    def __str__(self):
        return self.nombre


class Activo(models.Model):
    """
    Clase base abstracta, equivalente a la clase Activo del proyecto de POO.
    ActivoRentaVariable y ActivoRentaFija heredan de esta (herencia de modelos).
    """
    cartera = models.ForeignKey(Cartera, on_delete=models.CASCADE, related_name="%(class)s_set")
    ticker = models.CharField(max_length=20)
    cantidad = models.FloatField(validators=[MinValueValidator(0.01)])
    precio = models.FloatField(validators=[MinValueValidator(0.01)])
    moneda = models.CharField(max_length=3, choices=MONEDA_CHOICES)

    class Meta:
        abstract = True

    def calcular_valor(self):
        return self.cantidad * self.precio

    def get_tipo(self):
        return "Activo"

    def __str__(self):
        return f"{self.ticker} ({self.moneda})"


class ActivoRentaVariable(Activo):
    """Equivalente a ActivoRentaVariable del proyecto de POO."""
    def get_tipo(self):
        return "Renta Variable"


class ActivoRentaFija(Activo):
    """
    Equivalente a ActivoRentaFija del proyecto de POO.
    Sobreescribe calcular_valor() porque en Argentina la renta fija
    cotiza cada 100 nominales (polimorfismo).
    """
    def calcular_valor(self):
        return (self.precio * self.cantidad) / 100

    def get_tipo(self):
        return "Renta Fija"