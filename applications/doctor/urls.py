from django.urls import path
from applications.doctor.views.cita_medica import AgendaSemanalView
from applications.doctor.views.cita_medica import CitasJsonView

from applications.doctor.views.horarioatencion import (
    HorarioAtencionListView,
    HorarioAtencionCreateView,
    HorarioAtencionUpdateView,
    HorarioAtencionDeleteView,
)

from applications.doctor.views.atencion import (
    AtencionListView,
    AtencionCreateView,
    AtencionUpdateView,
    AtencionDeleteView
)

from applications.doctor.views.detalle_atencion import (
    DetalleAtencionListView,
    DetalleAtencionCreateView,
    DetalleAtencionUpdateView,
    DetalleAtencionDeleteView,
)

from applications.doctor.views.servicios_adicionales import (
    ServiciosAdicionalesListView,
    ServiciosAdicionalesCreateView,
    ServiciosAdicionalesUpdateView,
    ServiciosAdicionalesDeleteView,
)

from applications.doctor.views.pago import (
    PagoListView,
    PagoCreateView,
    PagoUpdateView,
    PagoDeleteView
)

from applications.doctor.views.detalle_pago import (
    DetallePagoListView,
    DetallePagoCreateView,
    DetallePagoUpdateView,
    DetallePagoDeleteView,
)

from applications.doctor.views.cita_medica import (
    CitaMedicaListView,
    CitaMedicaCreateView,
    CitaMedicaUpdateView,
    CitaMedicaDeleteView,
    AgendaSemanalView,
    CitasJsonView,
    PacientesJsonView,
    CitaMedicaApiCreateView,
    CitaMedicaApiUpdateView,
    CitaMedicaApiDeleteView
)

app_name = 'doctor'

urlpatterns = [
    #Horarios de atención
    path('horarios/', HorarioAtencionListView.as_view(), name='horarioatencion_list'),
    path('horarios/nuevo/', HorarioAtencionCreateView.as_view(), name='horarioatencion_create'),
    path('horarios/editar/<int:pk>/', HorarioAtencionUpdateView.as_view(), name='horarioatencion_update'),
    path('horarios/eliminar/<int:pk>/', HorarioAtencionDeleteView.as_view(), name='horarioatencion_delete'),
    
    #Citas Médicas (vistas tradicionales)
    path('citas/', CitaMedicaListView.as_view(), name='citamedica_list'),
    path('citas/nuevo/', CitaMedicaCreateView.as_view(), name='citamedica_create'),
    path('citas/editar/<int:pk>/', CitaMedicaUpdateView.as_view(), name='citamedica_update'),
    path('citas/eliminar/<int:pk>/', CitaMedicaDeleteView.as_view(), name='citamedica_delete'),
    
    #Atenciones
    path('atenciones/', AtencionListView.as_view(), name='atencion_list'),
    path('atenciones/crear/', AtencionCreateView.as_view(), name='atencion_create'),
    path('atenciones/editar/<int:pk>/', AtencionUpdateView.as_view(), name='atencion_update'),
    path('atenciones/eliminar/<int:pk>/', AtencionDeleteView.as_view(), name='atencion_delete'),
    
    #Detalle de Atenciones
    path('detalleatencion/', DetalleAtencionListView.as_view(), name='detalleatencion_list'),
    path('detalleatencion/create/', DetalleAtencionCreateView.as_view(), name='detalleatencion_create'),
    path('detalleatencion/update/<int:pk>/', DetalleAtencionUpdateView.as_view(), name='detalleatencion_update'),
    path('detalleatencion/delete/<int:pk>/', DetalleAtencionDeleteView.as_view(), name='detalleatencion_delete'),
    
    #Servicios Adicionales
    path('serviciosadicionales/', ServiciosAdicionalesListView.as_view(), name='serviciosadicionales_list'),
    path('serviciosadicionales/create/', ServiciosAdicionalesCreateView.as_view(), name='serviciosadicionales_create'),
    path('serviciosadicionales/update/<int:pk>/', ServiciosAdicionalesUpdateView.as_view(), name='serviciosadicionales_update'),
    path('serviciosadicionales/delete/<int:pk>/', ServiciosAdicionalesDeleteView.as_view(), name='serviciosadicionales_delete'),
    
    #Pagos
    path('pago/', PagoListView.as_view(), name='pago_list'),
    path('pago/create/', PagoCreateView.as_view(), name='pago_create'),
    path('pago/update/<int:pk>/', PagoUpdateView.as_view(), name='pago_update'),
    path('pago/delete/<int:pk>/', PagoDeleteView.as_view(), name='pago_delete'),
    
    #Detalle pago
    path('detallepago/', DetallePagoListView.as_view(), name='detallepago_list'),
    path('detallepago/create/', DetallePagoCreateView.as_view(), name='detallepago_create'),
    path('detallepago/update/<int:pk>/', DetallePagoUpdateView.as_view(), name='detallepago_update'),
    path('detallepago/delete/<int:pk>/', DetallePagoDeleteView.as_view(), name='detallepago_delete'),

    # Agenda semanal
    path('agenda/', AgendaSemanalView.as_view(), name='agenda_semanal'),
    
    # APIs JSON para el frontend (CORREGIDAS)
    path('api/citas/', CitasJsonView.as_view(), name='api_citas'),
    path('api/pacientes/', PacientesJsonView.as_view(), name='api_pacientes'),
    path('api/citas/crear/', CitaMedicaApiCreateView.as_view(), name='api_citas_crear'),

    
    # CORREGIDO: Separar las rutas para actualizar y eliminar
    path('api/citas/actualizar/<int:pk>/', CitaMedicaApiUpdateView.as_view(), name='api_citas_actualizar'),
    path('api/citas/eliminar/<int:pk>/', CitaMedicaApiDeleteView.as_view(), name='api_citas_eliminar'),

]










