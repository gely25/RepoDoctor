from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from applications.doctor.models import DetalleAtencion
from applications.doctor.forms.detalle_atencion import DetalleAtencionForm
from applications.security.components.mixin_crud import (
    CreateViewMixin, DeleteViewMixin, ListViewMixin, 
    PermissionMixin, UpdateViewMixin
)


class DetalleAtencionListView(PermissionMixin, ListViewMixin, ListView):
    template_name = 'doctor/detalleatencion/list.html'
    model = DetalleAtencion
    context_object_name = 'detalles'
    permission_required = 'doctor.view_detalleatencion'

    def get_queryset(self):
        q1 = self.request.GET.get('q')
        if q1:
            self.query.add(Q(medicamento__nombre__icontains=q1), Q.OR)
        return self.model.objects.filter(self.query).order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('doctor:detalleatencion_create')
        return context


class DetalleAtencionCreateView(PermissionMixin, CreateViewMixin, CreateView):
    model = DetalleAtencion
    form_class = DetalleAtencionForm
    template_name = 'doctor/detalleatencion/form.html'
    success_url = reverse_lazy('doctor:detalleatencion_list')
    permission_required = 'doctor.add_detalleatencion'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Registrar Prescripción'
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Prescripción registrada correctamente.")
        return response


class DetalleAtencionUpdateView(PermissionMixin, UpdateViewMixin, UpdateView):
    model = DetalleAtencion
    form_class = DetalleAtencionForm
    template_name = 'doctor/detalleatencion/form.html'
    success_url = reverse_lazy('doctor:detalleatencion_list')
    permission_required = 'doctor.change_detalleatencion'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Actualizar Prescripción'
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Prescripción actualizada correctamente.")
        return response


class DetalleAtencionDeleteView(PermissionMixin, DeleteViewMixin, DeleteView):
    model = DetalleAtencion
    template_name = 'core/delete.html'
    success_url = reverse_lazy('doctor:detalleatencion_list')
    permission_required = 'doctor.delete_detalleatencion'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Eliminar Prescripción'
        context['description'] = f"¿Desea eliminar la prescripción de {self.object.medicamento}?"
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        nombre = str(self.object.medicamento)
        response = super().form_valid(form)
        messages.success(self.request, f"Prescripción de {nombre} eliminada correctamente.")
        return response
