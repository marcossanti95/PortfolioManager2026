from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages

from .models import Perfil, Cartera, ActivoRentaVariable, ActivoRentaFija
from .forms import CarteraForm, ActivoRentaVariableForm, ActivoRentaFijaForm


def registro(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            Perfil.objects.create(usuario=usuario)
            login(request, usuario)
            messages.success(request, "¡Cuenta creada con éxito!")
            return redirect("dashboard")
    else:
        form = UserCreationForm()
    return render(request, "portfolio/registro.html", {"form": form})


@login_required
def dashboard(request):
    perfil, _ = Perfil.objects.get_or_create(usuario=request.user)
    carteras = perfil.carteras.all()
    return render(request, "portfolio/dashboard.html", {"carteras": carteras})


@login_required
def crear_cartera(request):
    perfil, _ = Perfil.objects.get_or_create(usuario=request.user)
    if request.method == "POST":
        form = CarteraForm(request.POST)
        if form.is_valid():
            cartera = form.save(commit=False)
            cartera.propietario = perfil
            cartera.save()
            messages.success(request, "Cartera creada correctamente.")
            return redirect("dashboard")
    else:
        form = CarteraForm()
    return render(request, "portfolio/crear_cartera.html", {"form": form})


@login_required
def detalle_cartera(request, cartera_id):
    perfil, _ = Perfil.objects.get_or_create(usuario=request.user)
    cartera = get_object_or_404(Cartera, id=cartera_id, propietario=perfil)
    activos = cartera.todos_los_activos()
    return render(request, "portfolio/detalle_cartera.html", {
        "cartera": cartera,
        "activos": activos,
    })


@login_required
def agregar_activo(request, cartera_id, tipo):
    perfil, _ = Perfil.objects.get_or_create(usuario=request.user)
    cartera = get_object_or_404(Cartera, id=cartera_id, propietario=perfil)

    FormClase = ActivoRentaVariableForm if tipo == "variable" else ActivoRentaFijaForm

    if request.method == "POST":
        form = FormClase(request.POST)
        if form.is_valid():
            activo = form.save(commit=False)
            activo.cartera = cartera
            activo.save()
            messages.success(request, "Activo agregado correctamente.")
            return redirect("detalle_cartera", cartera_id=cartera.id)
    else:
        form = FormClase()

    return render(request, "portfolio/agregar_activo.html", {
        "form": form,
        "cartera": cartera,
        "tipo": tipo,
    })