from django.contrib import admin
from APP1.models import Empleado
# Register your models here.

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'email', 'fono']

#registrar los modelos en el admin
admin.site.register(Empleado, EmpleadoAdmin)