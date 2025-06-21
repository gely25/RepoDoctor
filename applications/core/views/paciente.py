from django.urls import reverse_lazy
from django.db.models import Q
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from applications.core.models import Paciente
from applications.core.forms.paciente import PacienteForm
from applications.security.components.mixin_crud import (
    PermissionMixin, ListViewMixin, CreateViewMixin, UpdateViewMixin, DeleteViewMixin
)


class PacienteListView(PermissionMixin, ListViewMixin, ListView):
    template_name = 'core/paciente/list.html'
    model = Paciente
    context_object_name = 'pacientes'
    permission_required = 'view_paciente'

    def get_queryset(self):
        q1 = self.request.GET.get('q')
        if q1:
            self.query.add(Q(nombres__icontains=q1) | Q(apellidos__icontains=q1), Q.OR)
        return self.model.objects.filter(self.query).order_by('id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('core:paciente_create')
        return context


class PacienteCreateView(PermissionMixin, CreateViewMixin, CreateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'core/paciente/form.html'
    success_url = reverse_lazy('core:paciente_list')
    permission_required = 'add_paciente'


class PacienteUpdateView(PermissionMixin, UpdateViewMixin, UpdateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'core/paciente/form.html'
    success_url = reverse_lazy('core:paciente_list')
    permission_required = 'change_paciente'


class PacienteDeleteView(PermissionMixin, DeleteViewMixin, DeleteView):
    model = Paciente
    template_name = 'delete.html'
    success_url = reverse_lazy('core:paciente_list')
    permission_required = 'delete_paciente'
