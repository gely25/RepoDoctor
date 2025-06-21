


from django.urls import path
from applications.core.views.cargo import (
    CargoListView,
    CargoCreateView,
    CargoUpdateView,
    CargoDeleteView
)


from applications.core.views.especialidad import (
    EspecialidadListView,
    EspecialidadCreateView,
    EspecialidadUpdateView,
    EspecialidadDeleteView
)


from applications.core.views.doctor import (
    DoctorListView, DoctorCreateView, DoctorUpdateView, DoctorDeleteView
)

from applications.core.views.empleado import(EmpleadoListView, EmpleadoCreateView, EmpleadoUpdateView, EmpleadoDeleteView
    
)
from applications.core.views.diagnostico import(DiagnosticoListView, DiagnosticoCreateView, DiagnosticoUpdateView, DiagnosticoDeleteView)

from applications.core.views.fotopaciente import(FotoPacienteListView, FotoPacienteCreateView, FotoPacienteUpdateView, FotoPacienteDeleteView)

from applications.core.views.gastomensual import(GastoMensualListView, GastoMensualCreateView, GastoMensualUpdateView, GastoMensualDeleteView)

from applications.core.views.marca_medicamento import (MarcaMedicamentoListView, MarcaMedicamentoCreateView, MarcaMedicamentoUpdateView, MarcaMedicamentoDeleteView)

from applications.core.views.medicamento import (MedicamentoListView, MedicamentoCreateView, MedicamentoUpdateView, MedicamentoDeleteView)

from applications.core.views.paciente import (PacienteListView, PacienteCreateView, PacienteUpdateView, PacienteDeleteView)

from applications.core.views.tipogasto import (TipoGastoListView, TipoGastoCreateView, TipoGastoUpdateView, TipoGastoDeleteView)

from applications.core.views.tiposangre import (TipoSangreListView, TipoSangreCreateView, TipoSangreUpdateView, TipoSangreDeleteView)

from applications.core.views.tipomedicamento import(TipoMedicamentoListView, TipoMedicamentoCreateView, TipoMedicamentoUpdateView, TipoMedicamentoDeleteView)

app_name = 'core'

urlpatterns = [
    path('cargos/', CargoListView.as_view(), name='cargo_list'),
    path('cargos/crear/', CargoCreateView.as_view(), name='cargo_create'),
    path('cargos/editar/<int:pk>/', CargoUpdateView.as_view(), name='cargo_update'),
    path('cargos/eliminar/<int:pk>/', CargoDeleteView.as_view(), name='cargo_delete'),
#especialidad
    path('especialidades/', EspecialidadListView.as_view(), name='especialidad_list'),
    path('especialidades/crear/', EspecialidadCreateView.as_view(), name='especialidad_create'),
    path('especialidades/editar/<int:pk>/', EspecialidadUpdateView.as_view(), name='especialidad_update'),
    path('especialidades/eliminar/<int:pk>/', EspecialidadDeleteView.as_view(), name='especialidad_delete'),
    
#doctor
    path('doctores/', DoctorListView.as_view(), name='doctor_list'),
    path('doctores/crear/', DoctorCreateView.as_view(), name='doctor_create'),
    path('doctores/editar/<int:pk>/', DoctorUpdateView.as_view(), name='doctor_update'),
    path('doctores/eliminar/<int:pk>/', DoctorDeleteView.as_view(), name='doctor_delete'),
    
    
    
# Empleado
    path('empleados/', EmpleadoListView.as_view(), name='empleado_list'),
    path('empleados/crear/', EmpleadoCreateView.as_view(), name='empleado_create'),
    path('empleados/editar/<int:pk>/', EmpleadoUpdateView.as_view(), name='empleado_update'),
    path('empleados/eliminar/<int:pk>/', EmpleadoDeleteView.as_view(), name='empleado_delete'),
    
    
# Diagnóstico
    path('diagnosticos/', DiagnosticoListView.as_view(), name='diagnostico_list'),
    path('diagnosticos/crear/', DiagnosticoCreateView.as_view(), name='diagnostico_create'),
    path('diagnosticos/editar/<int:pk>/', DiagnosticoUpdateView.as_view(), name='diagnostico_update'),
    path('diagnosticos/eliminar/<int:pk>/', DiagnosticoDeleteView.as_view(), name='diagnostico_delete'),
    
    
# FotoPaciente
    path('fotos/', FotoPacienteListView.as_view(), name='fotopaciente_list'),
    path('fotos/crear/', FotoPacienteCreateView.as_view(), name='fotopaciente_create'),
    path('fotos/editar/<int:pk>/', FotoPacienteUpdateView.as_view(), name='fotopaciente_update'),
    path('fotos/eliminar/<int:pk>/', FotoPacienteDeleteView.as_view(), name='fotopaciente_delete'),
    
    
 # gasto mensual
    path('gastos/', GastoMensualListView.as_view(), name='gastomensual_list'),
    path('gastos/crear/', GastoMensualCreateView.as_view(), name='gastomensual_create'),
    path('gastos/editar/<int:pk>/', GastoMensualUpdateView.as_view(), name='gastomensual_update'),
    path('gastos/eliminar/<int:pk>/', GastoMensualDeleteView.as_view(), name='gastomensual_delete'),



#marca medicamento
    path('marcas/', MarcaMedicamentoListView.as_view(), name='marca_list'),
    path('marcas/crear/', MarcaMedicamentoCreateView.as_view(), name='marca_create'),
    path('marcas/editar/<int:pk>/', MarcaMedicamentoUpdateView.as_view(), name='marca_update'),
    path('marcas/eliminar/<int:pk>/', MarcaMedicamentoDeleteView.as_view(), name='marca_delete'),


#medicamento

    path('medicamentos/', MedicamentoListView.as_view(), name='medicamento_list'),
    path('medicamentos/crear/', MedicamentoCreateView.as_view(), name='medicamento_create'),
    path('medicamentos/editar/<int:pk>/', MedicamentoUpdateView.as_view(), name='medicamento_update'),
    path('medicamentos/eliminar/<int:pk>/', MedicamentoDeleteView.as_view(), name='medicamento_delete'),


# Paciente
    path('pacientes/', PacienteListView.as_view(), name='paciente_list'),
    path('pacientes/crear/', PacienteCreateView.as_view(), name='paciente_create'),
    path('pacientes/editar/<int:pk>/', PacienteUpdateView.as_view(), name='paciente_update'),
    path('pacientes/eliminar/<int:pk>/', PacienteDeleteView.as_view(), name='paciente_delete'),


# TipoGasto
    path('tipogastos/', TipoGastoListView.as_view(), name='tipogasto_list'),
    path('tipogastos/crear/', TipoGastoCreateView.as_view(), name='tipogasto_create'),
    path('tipogastos/editar/<int:pk>/', TipoGastoUpdateView.as_view(), name='tipogasto_update'),
    path('tipogastos/eliminar/<int:pk>/', TipoGastoDeleteView.as_view(), name='tipogasto_delete'),

        

# Tipo de Sangre
    path('tiposangre/', TipoSangreListView.as_view(), name='tiposangre_list'),
    path('tiposangre/crear/', TipoSangreCreateView.as_view(), name='tiposangre_create'),
    path('tiposangre/editar/<int:pk>/', TipoSangreUpdateView.as_view(), name='tiposangre_update'),
    path('tiposangre/eliminar/<int:pk>/', TipoSangreDeleteView.as_view(), name='tiposangre_delete'),

# Tipo de Medicamento
    path('tipomedicamentos/', TipoMedicamentoListView.as_view(), name='tipomedicamento_list'),
    path('tipomedicamentos/nuevo/', TipoMedicamentoCreateView.as_view(), name='tipomedicamento_create'),
    path('tipomedicamentos/editar/<int:pk>/', TipoMedicamentoUpdateView.as_view(), name='tipomedicamento_update'),
    path('tipomedicamentos/eliminar/<int:pk>/', TipoMedicamentoDeleteView.as_view(), name='tipomedicamento_delete'),

        
]




