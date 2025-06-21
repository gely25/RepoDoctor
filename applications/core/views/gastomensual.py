from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Q
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from applications.core.models import GastoMensual
from applications.core.forms.gastomensual import GastoMensualForm
from applications.security.components.mixin_crud import PermissionMixin, ListViewMixin, CreateViewMixin, UpdateViewMixin, DeleteViewMixin


class GastoMensualListView(PermissionMixin, ListViewMixin, ListView):
    model = GastoMensual
    template_name = 'core/gastomensual/list.html'
    context_object_name = 'gastos'
    permission_required = 'view_gastomensual'

    def get_queryset(self):
        q1 = self.request.GET.get('q')
        if q1:
            self.query.add(Q(descripcion__icontains=q1), Q.OR)
        return self.model.objects.filter(self.query).order_by('-fecha')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('core:gastomensual_create')
        return context


class GastoMensualCreateView(PermissionMixin, CreateViewMixin, CreateView):
    model = GastoMensual
    form_class = GastoMensualForm
    template_name = 'core/gastomensual/form.html'
    success_url = reverse_lazy('core:gastomensual_list')
    permission_required = 'add_gastomensual'

    def form_valid(self, form):
        messages.success(self.request, 'Gasto mensual registrado exitosamente.')
        return super().form_valid(form)


class GastoMensualUpdateView(PermissionMixin, UpdateViewMixin, UpdateView):
    model = GastoMensual
    form_class = GastoMensualForm
    template_name = 'core/gastomensual/form.html'
    success_url = reverse_lazy('core:gastomensual_list')
    permission_required = 'change_gastomensual'

    def form_valid(self, form):
        messages.success(self.request, 'Gasto mensual actualizado correctamente.')
        return super().form_valid(form)


class GastoMensualDeleteView(PermissionMixin, DeleteViewMixin, DeleteView):
    model = GastoMensual
    template_name = 'core/delete.html'
    success_url = reverse_lazy('core:gastomensual_list')
    permission_required = 'delete_gastomensual'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['grabar'] = 'Eliminar Gasto'
        context['description'] = f"¿Desea eliminar el gasto: {self.object.descripcion}?"
        context['back_url'] = self.success_url
        return context
