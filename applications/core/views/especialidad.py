from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Q
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from applications.security.components.mixin_crud import PermissionMixin, ListViewMixin, CreateViewMixin, UpdateViewMixin, DeleteViewMixin
from applications.core.models import EspecialidadMedica
from applications.core.forms.especialidad import EspecialidadMedicaForm  # lo crearemos en el paso 3

class EspecialidadListView(PermissionMixin, ListViewMixin, ListView):
    model = EspecialidadMedica
    template_name = 'core/especialidad/list.html'
    context_object_name = 'especialidades'
    permission_required = 'view_especialidadmedica'

    def get_queryset(self):
        q1 = self.request.GET.get('q')
        if q1:
            self.query.add(Q(nombre__icontains=q1), Q.OR)
        return self.model.objects.filter(self.query).order_by('id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['create_url'] = reverse_lazy('core:especialidad_create')
        return context

class EspecialidadCreateView(PermissionMixin, CreateViewMixin, CreateView):
    model = EspecialidadMedica
    form_class = EspecialidadMedicaForm
    template_name = 'core/especialidad/form.html'
    success_url = reverse_lazy('core:especialidad_list')
    permission_required = 'add_especialidadmedica'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Registrar Especialidad'
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f"Especialidad '{self.object.nombre}' registrada exitosamente.")
        return response

class EspecialidadUpdateView(PermissionMixin, UpdateViewMixin, UpdateView):
    model = EspecialidadMedica
    form_class = EspecialidadMedicaForm
    template_name = 'core/especialidad/form.html'
    success_url = reverse_lazy('core:especialidad_list')
    permission_required = 'change_especialidadmedica'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Actualizar Especialidad'
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f"Especialidad '{self.object.nombre}' actualizada exitosamente.")
        return response

class EspecialidadDeleteView(PermissionMixin, DeleteViewMixin, DeleteView):
    model = EspecialidadMedica
    template_name = 'core/delete.html'
    success_url = reverse_lazy('core:especialidad_list')
    permission_required = 'delete_especialidadmedica'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Eliminar Especialidad'
        context['description'] = f"¿Desea eliminar la especialidad: {self.object.nombre}?"
        context['back_url'] = self.success_url
        return context
