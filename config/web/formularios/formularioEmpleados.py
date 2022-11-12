from logging import PlaceHolder
from django import forms

class FormularioRegistroEmpleados(forms.Form):

    EMPLEADOS=(
        (1, 'Cocinero'),
        (2, 'Mesero'),
        (3, 'Bartender'),
        (4, 'Caja')
    )

    cedulaEmpleado=forms.CharField(
        widget=forms.NumberInput(attrs={"class":"form-control mb-3"}),
        required=True,
        label="Documento de identificacion"
    )
    nombreEmpleado=forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control mb-3"}),
        max_length=25,
        required=True,
        label="Nombre:"
    )
    direccionEmpleado=forms.CharField(
        widget=forms.Textarea(attrs={"class":"form-control mb-3"}),
        max_length=50,
        required=True,
        label="Dirección"
    )
    telefonoEmpleado=forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control mb-3"}),
        max_length=200,
        required=True,
        label="Teléfono:"
    )

    rolEmpleado=forms.ChoiceField(
        widget=forms.Select(attrs={"class":"form-control mb-3"}),
        choices=EMPLEADOS,
        label="Rol:"
    )

    