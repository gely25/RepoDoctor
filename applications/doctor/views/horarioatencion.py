from django.urls import reverse_lazy
from django.db.models import Q
from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from applications.doctor.models import HorarioAtencion
from applications.doctor.forms.horarioatencion import HorarioAtencionForm
from applications.security.components.mixin_crud import (
    PermissionMixin, ListViewMixin, CreateViewMixin, UpdateViewMixin, DeleteViewMixin
)


class HorarioAtencionListView(PermissionMixin, ListViewMixin, ListView):
    template_name = 'doctor/horarioatencion/list.html'
    model = HorarioAtencion
    context_object_name = 'horarios'
    permission_required = 'view_horarioatencion'

    def get_queryset(self):
        q1 = self.request.GET.get('q')
        if q1:
            self.query.add(Q(dia_semana__icontains=q1), Q.OR)
        return self.model.objects.filter(self.query).order_by('dia_semana', 'hora_inicio')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('doctor:horarioatencion_create')
        return context


class HorarioAtencionCreateView(PermissionMixin, CreateViewMixin, CreateView):
    model = HorarioAtencion
    form_class = HorarioAtencionForm
    template_name = 'doctor/horarioatencion/form.html'
    success_url = reverse_lazy('doctor:horarioatencion_list')
    permission_required = 'add_horarioatencion'

    def form_valid(self, form):
        messages.success(self.request, 'Horario de atención registrado correctamente.')
        return super().form_valid(form)


class HorarioAtencionUpdateView(PermissionMixin, UpdateViewMixin, UpdateView):
    model = HorarioAtencion
    form_class = HorarioAtencionForm
    template_name = 'doctor/horarioatencion/form.html'
    success_url = reverse_lazy('doctor:horarioatencion_list')
    permission_required = 'change_horarioatencion'

    def form_valid(self, form):
        messages.success(self.request, 'Horario de atención actualizado correctamente.')
        return super().form_valid(form)


class HorarioAtencionDeleteView(PermissionMixin, DeleteViewMixin, DeleteView):
    model = HorarioAtencion
    template_name = 'doctor/delete.html'
    success_url = reverse_lazy('doctor:horarioatencion_list')
    permission_required = 'delete_horarioatencion'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Eliminar Horario'
        context['description'] = f"¿Desea eliminar el horario del día {self.object.dia_semana} ({self.object.hora_inicio} - {self.object.hora_fin})?"
        context['back_url'] = self.success_url
        return context
