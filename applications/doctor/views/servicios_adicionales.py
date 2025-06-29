from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.db.models import Q

from applications.doctor.models import ServiciosAdicionales
from applications.doctor.forms.servicios_adicionales import ServiciosAdicionalesForm
from applications.security.components.mixin_crud import (
    PermissionMixin,
    ListViewMixin,
    CreateViewMixin,
    UpdateViewMixin,
    DeleteViewMixin
)


class ServiciosAdicionalesListView(PermissionMixin, ListViewMixin, ListView):
    model = ServiciosAdicionales
    template_name = 'doctor/serviciosadicionales/list.html'
    context_object_name = 'servicios'
    permission_required = 'view_serviciosadicionales'

    def get_queryset(self):
        q1 = self.request.GET.get('q')
        if q1 is not None:
            self.query.add(Q(nombre_servicio__icontains=q1), Q.OR)
        return self.model.objects.filter(self.query).order_by('id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['create_url'] = reverse_lazy('doctor:serviciosadicionales_create')
        return context


class ServiciosAdicionalesCreateView(PermissionMixin, CreateViewMixin, CreateView):
    model = ServiciosAdicionales
    template_name = 'doctor/serviciosadicionales/form.html'
    form_class = ServiciosAdicionalesForm
    success_url = reverse_lazy('doctor:serviciosadicionales_list')
    permission_required = 'add_serviciosadicionales'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Registrar Servicio'
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        obj = self.object
        messages.success(self.request, f"Éxito al crear el servicio: {obj.nombre_servicio}.")
        return response


class ServiciosAdicionalesUpdateView(PermissionMixin, UpdateViewMixin, UpdateView):
    model = ServiciosAdicionales
    template_name = 'doctor/serviciosadicionales/form.html'
    form_class = ServiciosAdicionalesForm
    success_url = reverse_lazy('doctor:serviciosadicionales_list')
    permission_required = 'change_serviciosadicionales'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Actualizar Servicio'
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        obj = self.object
        messages.success(self.request, f"Éxito al actualizar el servicio: {obj.nombre_servicio}.")
        return response


class ServiciosAdicionalesDeleteView(PermissionMixin, DeleteViewMixin, DeleteView):
    model = ServiciosAdicionales
    template_name = 'core/delete.html'
    success_url = reverse_lazy('doctor:serviciosadicionales_list')
    permission_required = 'delete_serviciosadicionales'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Eliminar Servicio'
        context['description'] = f"¿Desea eliminar el servicio: {self.object.nombre_servicio}?"
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        servicio = self.object.nombre_servicio
        response = super().form_valid(form)
        messages.success(self.request, f"Éxito al eliminar el servicio: {servicio}.")
        return response
