from django.shortcuts import render
from APP1.models import Empleado
from django.shortcuts import render
from . import forms

# Create your views here.
def empleadosData(request):
    empleados = Empleado.objects.all()
    data = {'empleados' : empleados}
    return render(request, 'empleados.html', data)

def userRegistrationView(request):
    form = forms.UserRegistrationForm()
    data = {'form':form}
    return render(request, 'userRegistration.html',data)