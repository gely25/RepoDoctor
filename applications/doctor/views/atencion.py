
from django.urls import reverse_lazy
from applications.doctor.models import Atencion
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from applications.doctor.forms.atencion import AtencionForm
from applications.security.components.mixin_crud import (
    PermissionMixin, ListViewMixin, CreateViewMixin,
    UpdateViewMixin, DeleteViewMixin
)
from django.contrib import messages


class AtencionListView(PermissionMixin, ListViewMixin, ListView):
    model = Atencion
    template_name = 'doctor/atencion/list.html'
    permission_required = 'doctor.view_atencion'
    context_object_name = 'atenciones'
    ordering = ['-fecha_atencion']
    title = 'Listado de Atenciones'
    title1 = 'Atenciones Médicas'
    back_url = reverse_lazy('doctor:atencion_list')


class AtencionCreateView(PermissionMixin, CreateViewMixin, CreateView):
    model = Atencion
    form_class = AtencionForm
    template_name = 'doctor/atencion/form_modern.html'
    success_url = reverse_lazy('doctor:atencion_list')
    permission_required = 'doctor.add_atencion'
    title = 'Nueva Atención Médica'
    title1 = 'Registrar Atención'
    back_url = reverse_lazy('doctor:atencion_list')

    def form_valid(self, form):
        messages.success(self.request, "Atención médica registrada correctamente.")
        return super().form_valid(form)


class AtencionUpdateView(PermissionMixin, UpdateViewMixin, UpdateView):
    model = Atencion
    form_class = AtencionForm
    template_name = 'doctor/atencion/form_modern.html'
    success_url = reverse_lazy('doctor:atencion_list')
    permission_required = 'doctor.change_atencion'
    title = 'Editar Atención Médica'
    title1 = 'Modificar Atención'
    back_url = reverse_lazy('doctor:atencion_list')

    def form_valid(self, form):
        messages.success(self.request, "Atención médica actualizada exitosamente.")
        return super().form_valid(form)


class AtencionDeleteView(PermissionMixin, DeleteViewMixin, DeleteView):
    model = Atencion
    template_name = 'delete.html'
    success_url = reverse_lazy('doctor:atencion_list')
    permission_required = 'doctor.delete_atencion'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Atención médica eliminada correctamente.")
        return super().delete(request, *args, **kwargs)
