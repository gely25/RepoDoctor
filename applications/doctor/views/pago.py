from django.contrib import messages
from django.urls import reverse_lazy
from django.db.models import Q
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from applications.security.components.mixin_crud import (
    CreateViewMixin, DeleteViewMixin, ListViewMixin,
    PermissionMixin, UpdateViewMixin
)
from applications.doctor.models import Pago
from applications.doctor.forms.pago import PagoForm  # Asegúrate de que esté bien la ruta

# LIST
class PagoListView(PermissionMixin, ListViewMixin, ListView):
    model = Pago
    template_name = 'doctor/pago/list.html'
    context_object_name = 'pagos'
    permission_required = 'view_pago'

    def get_queryset(self):
        q1 = self.request.GET.get('q')
        if q1:
            self.query.add(
                Q(atencion__paciente__nombres__icontains=q1) |
                Q(nombre_pagador__icontains=q1),
                Q.OR
            )
        return self.model.objects.filter(self.query).order_by('-fecha_creacion')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['create_url'] = reverse_lazy('doctor:pago_create')
        return context


# CREATE
class PagoCreateView(PermissionMixin, CreateViewMixin, CreateView):
    model = Pago
    form_class = PagoForm
    template_name = 'doctor/pago/form.html'
    success_url = reverse_lazy('doctor:pago_list')
    permission_required = 'add_pago'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Registrar Pago'
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f"Pago registrado exitosamente por {self.object.nombre_pagador or 'atención'}.")
        return response


# UPDATE
class PagoUpdateView(PermissionMixin, UpdateViewMixin, UpdateView):
    model = Pago
    form_class = PagoForm
    template_name = 'doctor/pago/form.html'
    success_url = reverse_lazy('doctor:pago_list')
    permission_required = 'change_pago'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Actualizar Pago'
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f"Pago actualizado correctamente.")
        return response


# DELETE
class PagoDeleteView(PermissionMixin, DeleteViewMixin, DeleteView):
    model = Pago
    template_name = 'core/delete.html'
    success_url = reverse_lazy('doctor:pago_list')
    permission_required = 'delete_pago'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Eliminar Pago'
        context['description'] = f"¿Desea eliminar el pago de {self.object.nombre_pagador or 'una atención médica'} por ${self.object.monto_total}?"
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        pago_ref = f"{self.object.nombre_pagador or 'atención'} - ${self.object.monto_total}"
        response = super().form_valid(form)
        messages.success(self.request, f"Pago eliminado correctamente: {pago_ref}.")
        return response
