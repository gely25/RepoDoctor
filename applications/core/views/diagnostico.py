from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Q
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from applications.core.models import Diagnostico
from applications.core.forms.diagnostico import DiagnosticoForm
from applications.security.components.mixin_crud import (
    PermissionMixin, ListViewMixin, CreateViewMixin, UpdateViewMixin, DeleteViewMixin
)

class DiagnosticoListView(PermissionMixin, ListViewMixin, ListView):
    model = Diagnostico
    template_name = 'core/diagnostico/list.html'
    context_object_name = 'diagnosticos'
    permission_required = 'view_diagnostico'

    def get_queryset(self):
        q1 = self.request.GET.get('q')
        if q1:
            self.query.add(Q(paciente__nombres__icontains=q1) | Q(paciente__apellidos__icontains=q1), Q.OR)
        return self.model.objects.filter(self.query).order_by('-fecha')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('core:diagnostico_create')
        return context


class DiagnosticoCreateView(PermissionMixin, CreateViewMixin, CreateView):
    model = Diagnostico
    form_class = DiagnosticoForm
    template_name = 'core/diagnostico/form.html'
    success_url = reverse_lazy('core:diagnostico_list')
    permission_required = 'add_diagnostico'

    def form_valid(self, form):
        messages.success(self.request, 'Diagnóstico registrado exitosamente.')
        return super().form_valid(form)


class DiagnosticoUpdateView(PermissionMixin, UpdateViewMixin, UpdateView):
    model = Diagnostico
    form_class = DiagnosticoForm
    template_name = 'core/diagnostico/form.html'
    success_url = reverse_lazy('core:diagnostico_list')
    permission_required = 'change_diagnostico'

    def form_valid(self, form):
        messages.success(self.request, 'Diagnóstico actualizado correctamente.')
        return super().form_valid(form)


class DiagnosticoDeleteView(PermissionMixin, DeleteViewMixin, DeleteView):
    model = Diagnostico
    template_name = 'core/delete.html'
    success_url = reverse_lazy('core:diagnostico_list')
    permission_required = 'delete_diagnostico'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['grabar'] = 'Eliminar Diagnóstico'
        context['description'] = f"¿Desea eliminar el diagnóstico del paciente: {self.object.paciente}?"
        context['back_url'] = self.success_url
        return context
