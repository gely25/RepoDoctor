from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Q
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from applications.core.models import Empleado
from applications.core.forms.empleado import EmpleadoForm
from applications.security.components.mixin_crud import PermissionMixin, ListViewMixin, CreateViewMixin, UpdateViewMixin, DeleteViewMixin

class EmpleadoListView(PermissionMixin, ListViewMixin, ListView):
    model = Empleado
    template_name = 'core/empleado/list.html'
    context_object_name = 'empleados'
    permission_required = 'view_empleado'

    def get_queryset(self):
        q1 = self.request.GET.get('q')
        if q1:
            self.query.add(Q(nombres__icontains=q1) | Q(apellidos__icontains=q1), Q.OR)
        return self.model.objects.filter(self.query).order_by('id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('core:empleado_create')
        return context

class EmpleadoCreateView(PermissionMixin, CreateViewMixin, CreateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'core/empleado/form.html'
    success_url = reverse_lazy('core:empleado_list')
    permission_required = 'add_empleado'

    def form_valid(self, form):
        messages.success(self.request, 'Empleado registrado exitosamente.')
        return super().form_valid(form)

class EmpleadoUpdateView(PermissionMixin, UpdateViewMixin, UpdateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'core/empleado/form.html'
    success_url = reverse_lazy('core:empleado_list')
    permission_required = 'change_empleado'

    def form_valid(self, form):
        messages.success(self.request, 'Empleado actualizado correctamente.')
        return super().form_valid(form)

class EmpleadoDeleteView(PermissionMixin, DeleteViewMixin, DeleteView):
    model = Empleado
    template_name = 'core/delete.html'
    success_url = reverse_lazy('core:empleado_list')
    permission_required = 'delete_empleado'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Eliminar Empleado'
        context['description'] = f"¿Desea eliminar al empleado: {self.object}?"
        context['back_url'] = self.success_url
        return context
