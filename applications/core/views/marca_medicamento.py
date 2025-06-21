from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from applications.core.models import MarcaMedicamento
from applications.core.forms.marca import MarcaMedicamentoForm
from applications.security.components.mixin_crud import (
    PermissionMixin, ListViewMixin, CreateViewMixin, UpdateViewMixin, DeleteViewMixin
)


class MarcaMedicamentoListView(PermissionMixin, ListViewMixin, ListView):
    model = MarcaMedicamento
    template_name = 'core/marca_medicamento/list.html'
    context_object_name = 'marcas'
    permission_required = 'view_marcamedicamento'

    def get_queryset(self):
        q1 = self.request.GET.get('q')
        if q1:
            self.query.add(Q(nombre__icontains=q1), Q.OR)
        return self.model.objects.filter(self.query).order_by('nombre')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('core:marca_create')
        return context


class MarcaMedicamentoCreateView(PermissionMixin, CreateViewMixin, CreateView):
    model = MarcaMedicamento
    form_class = MarcaMedicamentoForm
    template_name = 'core/marca_medicamento/form.html'
    success_url = reverse_lazy('core:marca_list')
    permission_required = 'add_marcamedicamento'

    def form_valid(self, form):
        messages.success(self.request, "Marca registrada exitosamente.")
        return super().form_valid(form)


class MarcaMedicamentoUpdateView(PermissionMixin, UpdateViewMixin, UpdateView):
    model = MarcaMedicamento
    form_class = MarcaMedicamentoForm
    template_name = 'core/marca_medicamento/form.html'
    success_url = reverse_lazy('core:marca_list')
    permission_required = 'change_marcamedicamento'

    def form_valid(self, form):
        messages.success(self.request, "Marca actualizada correctamente.")
        return super().form_valid(form)


class MarcaMedicamentoDeleteView(PermissionMixin, DeleteViewMixin, DeleteView):
    model = MarcaMedicamento
    template_name = 'delete.html'
    success_url = reverse_lazy('core:marca_list')
    permission_required = 'delete_marcamedicamento'
