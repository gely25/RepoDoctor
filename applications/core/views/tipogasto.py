from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Q
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from applications.core.models import TipoGasto
from applications.core.forms.tipogasto import TipoGastoForm
from applications.security.components.mixin_crud import (
    PermissionMixin, ListViewMixin, CreateViewMixin, UpdateViewMixin, DeleteViewMixin
)

class TipoGastoListView(PermissionMixin, ListViewMixin, ListView):
    model = TipoGasto
    template_name = 'core/tipogasto/list.html'
    context_object_name = 'tipogastos'
    permission_required = 'view_tipogasto'

    def get_queryset(self):
        q1 = self.request.GET.get('q')
        if q1:
            self.query.add(Q(nombre__icontains=q1), Q.OR)
        return self.model.objects.filter(self.query).order_by('id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('core:tipogasto_create')
        return context


class TipoGastoCreateView(PermissionMixin, CreateViewMixin, CreateView):
    model = TipoGasto
    form_class = TipoGastoForm
    template_name = 'core/tipogasto/form.html'
    success_url = reverse_lazy('core:tipogasto_list')
    permission_required = 'add_tipogasto'

    def form_valid(self, form):
        messages.success(self.request, 'Tipo de gasto registrado exitosamente.')
        return super().form_valid(form)


class TipoGastoUpdateView(PermissionMixin, UpdateViewMixin, UpdateView):
    model = TipoGasto
    form_class = TipoGastoForm
    template_name = 'core/tipogasto/form.html'
    success_url = reverse_lazy('core:tipogasto_list')
    permission_required = 'change_tipogasto'

    def form_valid(self, form):
        messages.success(self.request, 'Tipo de gasto actualizado correctamente.')
        return super().form_valid(form)


class TipoGastoDeleteView(PermissionMixin, DeleteViewMixin, DeleteView):
    model = TipoGasto
    template_name = 'core/delete.html'
    success_url = reverse_lazy('core:tipogasto_list')
    permission_required = 'delete_tipogasto'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Eliminar Tipo de Gasto'
        context['description'] = f"¿Desea eliminar el tipo de gasto: {self.object.nombre}?"
        context['back_url'] = self.success_url
        return context
