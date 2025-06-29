
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.db.models import Q

from applications.security.components.mixin_crud import (
    PermissionMixin, ListViewMixin, CreateViewMixin, UpdateViewMixin, DeleteViewMixin
)
from applications.doctor.models import DetallePago
from applications.doctor.forms.detalle_pago import DetallePagoForm


class DetallePagoListView(PermissionMixin, ListViewMixin, ListView):
    template_name = 'doctor/detallepago/list.html'
    model = DetallePago
    context_object_name = 'detalles_pago'
    permission_required = 'view_detallepago'

    def get_queryset(self):
        q1 = self.request.GET.get('q')
        if q1:
            self.query.add(Q(servicio_adicional__nombre__icontains=q1), Q.OR)
        return self.model.objects.filter(self.query).select_related('pago', 'servicio_adicional').order_by('id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('doctor:detallepago_create')
        return context


class DetallePagoCreateView(PermissionMixin, CreateViewMixin, CreateView):
    model = DetallePago
    template_name = 'doctor/detallepago/form.html'
    form_class = DetallePagoForm
    success_url = reverse_lazy('doctor:detallepago_list')
    permission_required = 'add_detallepago'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Registrar Detalle de Pago'
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        detalle = self.object
        messages.success(self.request, f"Éxito al crear el detalle: {detalle.servicio_adicional}.")
        return response


class DetallePagoUpdateView(PermissionMixin, UpdateViewMixin, UpdateView):
    model = DetallePago
    template_name = 'doctor/detallepago/form.html'
    form_class = DetallePagoForm
    success_url = reverse_lazy('doctor:detallepago_list')
    permission_required = 'change_detallepago'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Actualizar Detalle de Pago'
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        detalle = self.object
        messages.success(self.request, f"Detalle actualizado: {detalle.servicio_adicional}.")
        return response


class DetallePagoDeleteView(PermissionMixin, DeleteViewMixin, DeleteView):
    model = DetallePago
    template_name = 'core/delete.html'
    success_url = reverse_lazy('doctor:detallepago_list')
    permission_required = 'delete_detallepago'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Eliminar Detalle de Pago'
        context['description'] = f"¿Deseas eliminar el servicio: {self.object.servicio_adicional}?"
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        servicio = self.object.servicio_adicional
        response = super().form_valid(form)
        messages.success(self.request, f"Detalle eliminado correctamente: {servicio}.")
        return response
