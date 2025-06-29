


from django.urls import path

from applications.core.views.tiposangre import (
    TipoSangreListView,
    TipoSangreCreateView,
    TipoSangreUpdateView,
    TipoSangreDeleteView,
)

from applications.core.views.paciente import (
    PacienteListView,
    PacienteCreateView,
    PacienteUpdateView,
    PacienteDeleteView,
)

from applications.core.views.doctor import (
    DoctorListView,
    DoctorCreateView,
    DoctorUpdateView,
    DoctorDeleteView,
)

from applications.core.views.cargo import (
    CargoListView,
    CargoCreateView,
    CargoUpdateView,
    CargoDeleteView,
)


from applications.core.views.empleado import (
    EmpleadoListView,
    EmpleadoCreateView,
    EmpleadoUpdateView,
    EmpleadoDeleteView,
)



from applications.core.views.tipomedicamento import (
    TipoMedicamentoListView,
    TipoMedicamentoCreateView,
    TipoMedicamentoUpdateView,
    TipoMedicamentoDeleteView,
)


from applications.core.views.marca_medicamento import (
    MarcaMedicamentoListView,
    MarcaMedicamentoCreateView,
    MarcaMedicamentoUpdateView,
    MarcaMedicamentoDeleteView,
)




from applications.core.views.medicamento import (
    MedicamentoListView,
    MedicamentoCreateView,
    MedicamentoUpdateView,
    MedicamentoDeleteView,
)


from applications.core.views.diagnostico import (
    DiagnosticoListView,
    DiagnosticoCreateView,
    DiagnosticoUpdateView,
    DiagnosticoDeleteView,
)


from applications.core.views.tipogasto import (
    TipoGastoListView, TipoGastoCreateView,
    TipoGastoUpdateView, TipoGastoDeleteView
)

from applications.core.views.gastomensual import (
    GastoMensualListView,
    GastoMensualCreateView,
    GastoMensualUpdateView,
    GastoMensualDeleteView
)


from applications.core.views.fotopaciente import (
    FotoPacienteListView,
    FotoPacienteCreateView,
    FotoPacienteUpdateView,
    FotoPacienteDeleteView
)

app_name = 'core'

urlpatterns = [
    #Sangre
    path('tiposangre/', TipoSangreListView.as_view(), name='tiposangre_list'),
    path('tiposangre/crear/', TipoSangreCreateView.as_view(), name='tiposangre_create'),
    path('tiposangre/editar/<int:pk>/', TipoSangreUpdateView.as_view(), name='tiposangre_update'),
    path('tiposangre/eliminar/<int:pk>/', TipoSangreDeleteView.as_view(), name='tiposangre_delete'),
    
    #Pacientes
    path('pacientes/', PacienteListView.as_view(), name='paciente_list'),
    path('pacientes/crear/', PacienteCreateView.as_view(), name='paciente_create'),
    path('pacientes/editar/<int:pk>/', PacienteUpdateView.as_view(), name='paciente_update'),
    path('pacientes/eliminar/<int:pk>/', PacienteDeleteView.as_view(), name='paciente_delete'),
     
    #Doctores
    path('doctores/', DoctorListView.as_view(), name='doctor_list'),
    path('doctores/crear/', DoctorCreateView.as_view(), name='doctor_create'),
    path('doctores/editar/<int:pk>/', DoctorUpdateView.as_view(), name='doctor_update'),
    path('doctores/eliminar/<int:pk>/', DoctorDeleteView.as_view(), name='doctor_delete'),
    
    #Cargos
    path('cargos/', CargoListView.as_view(), name='cargo_list'),
    path('cargos/crear/', CargoCreateView.as_view(), name='cargo_create'),
    path('cargos/editar/<int:pk>/', CargoUpdateView.as_view(), name='cargo_update'),
    path('cargos/eliminar/<int:pk>/', CargoDeleteView.as_view(), name='cargo_delete'),
    
    #Empleados
    path('empleados/', EmpleadoListView.as_view(), name='empleado_list'),
    path('empleados/nuevo/', EmpleadoCreateView.as_view(), name='empleado_create'),
    path('empleados/editar/<int:pk>/', EmpleadoUpdateView.as_view(), name='empleado_update'),
    path('empleados/eliminar/<int:pk>/', EmpleadoDeleteView.as_view(), name='empleado_delete'),
    
    #Tipo de Medicamento
    
    path('tipomedicamento/', TipoMedicamentoListView.as_view(), name='tipomedicamento_list'),
    path('tipomedicamento/create/', TipoMedicamentoCreateView.as_view(), name='tipomedicamento_create'),
    path('tipomedicamento/update/<int:pk>/', TipoMedicamentoUpdateView.as_view(), name='tipomedicamento_update'),
    path('tipomedicamento/delete/<int:pk>/', TipoMedicamentoDeleteView.as_view(), name='tipomedicamento_delete'),
    
    # Marca Medicamento
    
    path('marca/', MarcaMedicamentoListView.as_view(), name='marca_list'),
    path('marca/crear/', MarcaMedicamentoCreateView.as_view(), name='marca_create'),
    path('marca/editar/<int:pk>/', MarcaMedicamentoUpdateView.as_view(), name='marca_update'),
    path('marca/eliminar/<int:pk>/', MarcaMedicamentoDeleteView.as_view(), name='marca_delete'),
    
    # Medicamentos 
    
    path('medicamentos/', MedicamentoListView.as_view(), name='medicamento_list'),
    path('medicamentos/create/', MedicamentoCreateView.as_view(), name='medicamento_create'),
    path('medicamentos/update/<int:pk>/', MedicamentoUpdateView.as_view(), name='medicamento_update'),
    path('medicamentos/delete/<int:pk>/', MedicamentoDeleteView.as_view(), name='medicamento_delete'),
    
    # Diagnosticos
    
    path('diagnosticos/', DiagnosticoListView.as_view(), name='diagnostico_list'),
    path('diagnosticos/crear/', DiagnosticoCreateView.as_view(), name='diagnostico_create'),
    path('diagnosticos/editar/<int:pk>/', DiagnosticoUpdateView.as_view(), name='diagnostico_update'),
    path('diagnosticos/eliminar/<int:pk>/', DiagnosticoDeleteView.as_view(), name='diagnostico_delete'),
    
    #Tipos de Gastos
    path('tipogasto/', TipoGastoListView.as_view(), name='tipogasto_list'),
    path('tipogasto/create/', TipoGastoCreateView.as_view(), name='tipogasto_create'),
    path('tipogasto/update/<int:pk>/', TipoGastoUpdateView.as_view(), name='tipogasto_update'),
    path('tipogasto/delete/<int:pk>/', TipoGastoDeleteView.as_view(), name='tipogasto_delete'),
    
    # Gastos
    path('gastomensual/', GastoMensualListView.as_view(), name='gastomensual_list'),
    path('gastomensual/crear/', GastoMensualCreateView.as_view(), name='gastomensual_create'),
    path('gastomensual/editar/<int:pk>/', GastoMensualUpdateView.as_view(), name='gastomensual_update'),
    path('gastomensual/eliminar/<int:pk>/', GastoMensualDeleteView.as_view(), name='gastomensual_delete'),
    
    #Fotos de Pacientes
    path('fotospaciente/', FotoPacienteListView.as_view(), name='fotopaciente_list'),
    path('fotospaciente/nuevo/', FotoPacienteCreateView.as_view(), name='fotopaciente_create'),
    path('fotospaciente/editar/<int:pk>/', FotoPacienteUpdateView.as_view(), name='fotopaciente_update'),
    path('fotospaciente/eliminar/<int:pk>/', FotoPacienteDeleteView.as_view(), name='fotopaciente_delete'),
    
    
]








