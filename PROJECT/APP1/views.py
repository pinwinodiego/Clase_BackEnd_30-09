from django.shortcuts import render
from APP1.models import Empleado

# Create your views here.
def empleadosData(request):
    empleados = Empleado.objects.all()
    data = {'empleados' : empleados}
    return render(request, 'empleados.html', data)
