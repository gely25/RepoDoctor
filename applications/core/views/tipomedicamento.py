from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.db.models import Q

from applications.security.components.mixin_crud import PermissionMixin, ListViewMixin, CreateViewMixin, UpdateViewMixin, DeleteViewMixin
from applications.core.models import TipoMedicamento
from applications.core.forms.tipomed import TipoMedicamentoForm


class TipoMedicamentoListView(PermissionMixin, ListViewMixin, ListView):
    template_name = 'core/tipomedicamento/list.html'
    model = TipoMedicamento
    context_object_name = 'tipomedicamentos'
    permission_required = 'view_tipomedicamento'

    def get_queryset(self):
        q1 = self.request.GET.get('q')
        if q1:
            self.query.add(Q(nombre__icontains=q1), Q.OR)
        return self.model.objects.filter(self.query).order_by('id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('core:tipomedicamento_create')
        return context


class TipoMedicamentoCreateView(PermissionMixin, CreateViewMixin, CreateView):
    model = TipoMedicamento
    form_class = TipoMedicamentoForm
    template_name = 'core/tipomedicamento/form.html'
    success_url = reverse_lazy('core:tipomedicamento_list')
    permission_required = 'add_tipomedicamento'

    def form_valid(self, form):
        messages.success(self.request, 'Tipo de medicamento registrado exitosamente.')
        return super().form_valid(form)


class TipoMedicamentoUpdateView(PermissionMixin, UpdateViewMixin, UpdateView):
    model = TipoMedicamento
    form_class = TipoMedicamentoForm
    template_name = 'core/tipomedicamento/form.html'
    success_url = reverse_lazy('core:tipomedicamento_list')
    permission_required = 'change_tipomedicamento'

    def form_valid(self, form):
        messages.success(self.request, 'Tipo de medicamento actualizado exitosamente.')
        return super().form_valid(form)


class TipoMedicamentoDeleteView(PermissionMixin, DeleteViewMixin, DeleteView):
    model = TipoMedicamento
    template_name = 'form/delete.html'
    success_url = reverse_lazy('core:tipomedicamento_list')
    permission_required = 'delete_tipomedicamento'
