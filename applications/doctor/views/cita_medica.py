from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView, View
from django.db.models import Q
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
import json
from datetime import date, timedelta, datetime
from applications.core.models import Paciente
from applications.doctor.models import CitaMedica
from applications.doctor.forms.cita_medica import CitaMedicaForm
from applications.security.components.mixin_crud import (
    PermissionMixin, ListViewMixin, CreateViewMixin, UpdateViewMixin, DeleteViewMixin
)


class CitaMedicaListView(PermissionMixin, ListViewMixin, ListView):
    model = CitaMedica
    template_name = 'doctor/citamedica/list.html'
    context_object_name = 'citamedicas'
    permission_required = 'doctor.view_citamedica'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return self.model.objects.filter(
                Q(paciente__nombres__icontains=query) | Q(paciente__apellidos__icontains=query)
            ).order_by('fecha', 'hora_cita')
        return self.model.objects.all().order_by('fecha', 'hora_cita')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('doctor:citamedica_create')
        return context


class CitaMedicaCreateView(PermissionMixin, CreateViewMixin, CreateView):
    model = CitaMedica
    form_class = CitaMedicaForm
    template_name = 'doctor/citamedica/form.html'
    success_url = reverse_lazy('doctor:citamedica_list')
    permission_required = 'doctor.add_citamedica'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['grabar'] = 'Grabar Cita'
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Éxito al registrar la cita médica.")
        return response
    
    def get_initial(self):
        initial = super().get_initial()
        initial['fecha'] = self.request.GET.get('fecha')
        initial['hora_cita'] = self.request.GET.get('hora')
        return initial


class CitaMedicaUpdateView(PermissionMixin, UpdateViewMixin, UpdateView):
    model = CitaMedica
    form_class = CitaMedicaForm
    template_name = 'doctor/citamedica/form.html'
    success_url = reverse_lazy('doctor:citamedica_list')
    permission_required = 'doctor.change_citamedica'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['grabar'] = 'Actualizar Cita'
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Éxito al actualizar la cita médica.")
        return response


class CitaMedicaDeleteView(PermissionMixin, DeleteViewMixin, DeleteView):
    model = CitaMedica
    template_name = 'core/delete.html'
    success_url = reverse_lazy('doctor:citamedica_list')
    permission_required = 'doctor.delete_citamedica'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['grabar'] = 'Eliminar Cita'
        context['description'] = f"¿Desea eliminar la cita médica del paciente {self.object.paciente.nombre_completo} del {self.object.fecha} a las {self.object.hora_cita}?"
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        cita = self.object
        response = super().form_valid(form)
        messages.success(self.request, f"Éxito al eliminar la cita del {cita.fecha} a las {cita.hora_cita}.")
        return response


# ========== NUEVAS VISTAS PARA LA AGENDA SEMANAL ==========

class AgendaSemanalView(PermissionMixin, TemplateView):
    template_name = 'doctor/citamedica/agenda_semanal.html'
    permission_required = 'doctor.view_citamedica'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Obtener offset de semana desde parámetros
        week_offset = int(self.request.GET.get('week_offset', 0))
        
        # Calcular semana actual + offset
        hoy = date.today()
        inicio_semana = hoy - timedelta(days=hoy.weekday()) + timedelta(weeks=week_offset)
        dias = [inicio_semana + timedelta(days=i) for i in range(5)]  # lunes a viernes

        # Horas visibles en la agenda
        horas = [f"{h:02d}:00" for h in range(8, 18)]  # de 08:00 a 17:00

        context['dias'] = dias
        context['horas'] = horas
        context['week_offset'] = week_offset
        return context


class CitasJsonView(PermissionMixin, View):
    permission_required = 'doctor.view_citamedica'
    
    def get(self, request):
        # Obtener offset de semana
        week_offset = int(request.GET.get('week_offset', 0))
        
        # Calcular fechas de la semana
        hoy = date.today()
        inicio_semana = hoy - timedelta(days=hoy.weekday()) + timedelta(weeks=week_offset)
        fin_semana = inicio_semana + timedelta(days=4)  # viernes
        
        # Generar lista de fechas
        dias = [inicio_semana + timedelta(days=i) for i in range(5)]
        
        # Obtener citas de la semana
        citas = CitaMedica.objects.filter(
            fecha__range=[inicio_semana, fin_semana]
        ).select_related('paciente')

        # Formatear datos para el frontend
        appointments = {}
        for cita in citas:
            appointments[str(cita.id)] = {
                "id": cita.id,
                "paciente": cita.paciente.nombre_completo,
                "paciente_id": cita.paciente.id,
                "fecha": str(cita.fecha),
                "hora": cita.hora_cita.strftime("%H:%M"),
                "estado": cita.estado,
                "observaciones": cita.observaciones or ""
            }

        return JsonResponse({
            'appointments': appointments,
            'week_dates': [str(dia) for dia in dias]
        })


class PacientesJsonView(PermissionMixin, View):
    permission_required = 'doctor.view_paciente'
    
    def get(self, request):
        pacientes = Paciente.objects.all().order_by('nombres', 'apellidos')
        
        data = {}
        for paciente in pacientes:
            data[str(paciente.id)] = {
                "id": paciente.id,
                "nombre_completo": paciente.nombre_completo,
                "nombres": paciente.nombres,
                "apellidos": paciente.apellidos
            }
        
        return JsonResponse(data)


@method_decorator(csrf_exempt, name='dispatch')
class CitaMedicaApiCreateView(PermissionMixin, View):
    permission_required = 'doctor.add_citamedica'
    
    def post(self, request):
        try:
            data = json.loads(request.body)
            
            # Validar datos requeridos
            required_fields = ['paciente', 'fecha', 'hora_cita', 'estado']
            for field in required_fields:
                if not data.get(field):
                    return JsonResponse({'error': f'Campo {field} es requerido'}, status=400)
            
            # Obtener paciente
            try:
                paciente = Paciente.objects.get(id=data['paciente'])
            except Paciente.DoesNotExist:
                return JsonResponse({'error': 'Paciente no encontrado'}, status=404)
            
            # Crear cita
            cita = CitaMedica.objects.create(
                paciente=paciente,
                fecha=data['fecha'],
                hora_cita=data['hora_cita'],
                estado=data['estado'],
                observaciones=data.get('observaciones', '')
            )
            
            return JsonResponse({
                'success': True,
                'message': 'Cita creada correctamente',
                'cita_id': cita.id
            })
            
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Datos JSON inválidos'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

@method_decorator(csrf_exempt, name='dispatch')
class CitaMedicaApiUpdateView(PermissionMixin, View):
    permission_required = 'doctor.change_citamedica'

    def put(self, request, pk):
        try:
            cita = get_object_or_404(CitaMedica, pk=pk)
            data = json.loads(request.body)

            # Obtener valores originales
            fecha_actual = cita.fecha
            hora_actual = cita.hora_cita

            # Leer datos nuevos, si vienen
            fecha_nueva_str = data.get('fecha')
            hora_nueva_str = data.get('hora_cita')

            # Si no se manda fecha/hora, usar las actuales
            fecha_nueva = datetime.strptime(fecha_nueva_str, '%Y-%m-%d').date() if fecha_nueva_str else fecha_actual
            hora_nueva = datetime.strptime(hora_nueva_str, '%H:%M').time() if hora_nueva_str else hora_actual

            # Verificar si hay cambio real en fecha u hora
            if (fecha_nueva != fecha_actual or hora_nueva != hora_actual):
                existe = CitaMedica.objects.filter(
                    fecha=fecha_nueva,
                    hora_cita=hora_nueva
                ).exclude(pk=cita.pk).exists()

                if existe:
                    return JsonResponse({
                        'error': f'Ya existe una cita programada para el {fecha_nueva} a las {hora_nueva.strftime("%H:%M")}'
                    }, status=400)

            # Aplicar cambios solo si vienen en el body
            if 'paciente' in data:
                try:
                    paciente = Paciente.objects.get(id=data['paciente'])
                    cita.paciente = paciente
                except Paciente.DoesNotExist:
                    return JsonResponse({'error': 'Paciente no encontrado'}, status=404)

            if fecha_nueva != fecha_actual:
                cita.fecha = fecha_nueva
            if hora_nueva != hora_actual:
                cita.hora_cita = hora_nueva

            if 'estado' in data:
                cita.estado = data['estado']
            if 'observaciones' in data:
                cita.observaciones = data['observaciones']

            cita.save()

            return JsonResponse({
                'success': True,
                'message': 'Cita actualizada correctamente'
            })

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Datos JSON inválidos'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)


@method_decorator(csrf_exempt, name='dispatch')
class CitaMedicaApiDeleteView(PermissionMixin, View):
    permission_required = 'doctor.delete_citamedica'
    
    def delete(self, request, pk):
        try:
            cita = get_object_or_404(CitaMedica, pk=pk)
            cita.delete()
            
            return JsonResponse({
                'success': True,
                'message': 'Cita eliminada correctamente'
            })
            
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)