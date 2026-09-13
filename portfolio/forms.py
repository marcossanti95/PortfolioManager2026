from django import forms
from .models import Cartera, ActivoRentaVariable, ActivoRentaFija


class CarteraForm(forms.ModelForm):
    class Meta:
        model = Cartera
        fields = ["nombre"]
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control", "placeholder": "Nombre de la cartera"}),
        }


class ActivoRentaVariableForm(forms.ModelForm):
    class Meta:
        model = ActivoRentaVariable
        fields = ["ticker", "cantidad", "precio", "moneda"]
        widgets = {
            "ticker": forms.TextInput(attrs={"class": "form-control"}),
            "cantidad": forms.NumberInput(attrs={"class": "form-control", "step": "0.01"}),
            "precio": forms.NumberInput(attrs={"class": "form-control", "step": "0.01"}),
            "moneda": forms.Select(attrs={"class": "form-control"}),
        }


class ActivoRentaFijaForm(forms.ModelForm):
    class Meta:
        model = ActivoRentaFija
        fields = ["ticker", "cantidad", "precio", "moneda"]
        widgets = {
            "ticker": forms.TextInput(attrs={"class": "form-control"}),
            "cantidad": forms.NumberInput(attrs={"class": "form-control", "step": "0.01"}),
            "precio": forms.NumberInput(attrs={"class": "form-control", "step": "0.01"}),
            "moneda": forms.Select(attrs={"class": "form-control"}),
        }