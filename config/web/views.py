from django.shortcuts import render
from web.formularios.formularioEmpleados import FormularioRegistroEmpleados
from web.formularios.formularioPlatos import FormularioRegistroPlatos
from web.models import Empleados, Platos

# Create your views here.

#CADA VISTA ES UNA FUNCION DE PY

def Home(request):
    return render(request,'index.html')

def PlatosVista(request):

    #cargar el formulario de registro de platos
    formulario=FormularioRegistroPlatos()

    #creamos un diccionario para enviar datos hacia el template
    diccinarioEnvioDatos={
        'formulario':formulario
    }

    #Recibiendo datos del formulario
    #PETICION DE TIPO POST 
    if request.method=='POST':
        datosFormulario=FormularioRegistroPlatos(request.POST)
        if datosFormulario.is_valid():
            datosLimpios=datosFormulario.cleaned_data
            #ENVIANDO DATOS A LA BASE DE DATOS
            platoNuevo=Platos(
                nombre=datosLimpios["nombrePlato"],
                descripcion=datosLimpios["descripcionPlato"],
                imagen=datosLimpios["fotoPlato"],
                precio=datosLimpios["precioPlato"],
                tipo=datosLimpios["tipoPlato"]
            )
            platoNuevo.save()

    return render(request,'platos.html',diccinarioEnvioDatos)
def EmpleadosVista(request):
    #cargar el formulario de registro de platos
    formularioEmpleados=FormularioRegistroEmpleados()

    #creamos un diccionario para enviar datos hacia el template
    diccinarioEnvioDatos={
        'formularioEmpleados':formularioEmpleados
    }

    #Recibiendo datos del formulario
    #PETICION DE TIPO POST 
    if request.method=='POST':
        datosFormulario=FormularioRegistroEmpleados(request.POST)
        if datosFormulario.is_valid():
            datosLimpios=datosFormulario.cleaned_data
            #ENVIANDO DATOS A LA BASE DE DATOS
            empleadoNuevo=Empleados(
            cedula=datosLimpios["cedulaEmpleado"],
            nombre=datosLimpios["nombreEmpleado"],
            direccion=datosLimpios["direccionEmpleado"],
            telefono=datosLimpios["telefonoEmpleado"],
            rol=datosLimpios["rolEmpleado"]
        )
        empleadoNuevo.save()
         

    return render(request,'empleados.html',diccinarioEnvioDatos)

    