from django.contrib import admin
from applications.core.models import (
    Paciente, TipoSangre, FotoPaciente, Doctor, Empleado, Cargo,
    EspecialidadMedica, Diagnostico, Medicamento, TipoMedicamento,
    MarcaMedicamento, TipoGasto, GastoMensual
)

from applications.core.forms.paciente import PacienteForm
from applications.core.forms.tiposangre import TipoSangreForm
from applications.core.forms.fotopaciente import FotoPacienteForm
from applications.core.forms.doctor import DoctorForm
from applications.core.forms.empleado import EmpleadoForm
from applications.core.forms.cargo import CargoForm
from applications.core.forms.especialidad import EspecialidadMedicaForm
from applications.core.forms.diagnostico import DiagnosticoForm
from applications.core.forms.medicamento import MedicamentoForm
from applications.core.forms.tipomed import TipoMedicamentoForm
from applications.core.forms.marca import MarcaMedicamentoForm
from applications.core.forms.tipogasto import TipoGastoForm
from applications.core.forms.gastomensual import GastoMensualForm



@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    form = PacienteForm
    list_display = ('nombres', 'apellidos', 'fecha_nacimiento', 'tipo_sangre')
    search_fields = ('nombres', 'apellidos')
    list_filter = ('tipo_sangre',)


@admin.register(TipoSangre)
class TipoSangreAdmin(admin.ModelAdmin):
    form = TipoSangreForm
    list_display = ('tipo',)
    search_fields = ('tipo',)


@admin.register(FotoPaciente)
class FotoPacienteAdmin(admin.ModelAdmin):
    form = FotoPacienteForm
    list_display = ('paciente', 'descripcion', 'fecha')
    search_fields = ('paciente__nombres', 'descripcion')
    list_filter = ('fecha',)


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    form = DoctorForm
    list_display = ('nombres', 'apellidos', 'especialidad', 'cargo')
    search_fields = ('nombres', 'apellidos')
    list_filter = ('especialidad', 'cargo')


@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    form = EmpleadoForm
    list_display = ('nombres', 'apellidos', 'cargo')
    search_fields = ('nombres', 'apellidos')
    list_filter = ('cargo',)


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    form = CargoForm
    list_display = ('nombre',)
    search_fields = ('nombre',)


@admin.register(EspecialidadMedica)
class EspecialidadMedicaAdmin(admin.ModelAdmin):
    form = EspecialidadMedicaForm
    list_display = ('nombre',)
    search_fields = ('nombre',)


@admin.register(Diagnostico)
class DiagnosticoAdmin(admin.ModelAdmin):
    form = DiagnosticoForm
    list_display = ('paciente', 'doctor', 'fecha')
    search_fields = ('paciente__nombres', 'doctor__nombres')
    list_filter = ('fecha',)


@admin.register(Medicamento)
class MedicamentoAdmin(admin.ModelAdmin):
    form = MedicamentoForm
    list_display = ('nombre', 'marca', 'tipo', 'stock')
    search_fields = ('nombre', 'descripcion')
    list_filter = ('marca', 'tipo')


@admin.register(MarcaMedicamento)
class MarcaMedicamentoAdmin(admin.ModelAdmin):
    form = MarcaMedicamentoForm
    list_display = ('nombre',)
    search_fields = ('nombre',)


@admin.register(TipoMedicamento)
class TipoMedicamentoAdmin(admin.ModelAdmin):
    form = TipoMedicamentoForm
    list_display = ('nombre',)
    search_fields = ('nombre',)


@admin.register(TipoGasto)
class TipoGastoAdmin(admin.ModelAdmin):
    form = TipoGastoForm
    list_display = ('nombre',)
    search_fields = ('nombre',)


@admin.register(GastoMensual)
class GastoMensualAdmin(admin.ModelAdmin):
    form = GastoMensualForm
    list_display = ('tipo', 'monto', 'fecha')
    search_fields = ('descripcion',)
    list_filter = ('tipo', 'fecha')


