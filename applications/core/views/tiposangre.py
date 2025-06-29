# applications/core/views/tipo_sangre_views.py
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Q
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from applications.core.models import TipoSangre
from applications.core.forms.tiposangre import TipoSangreForm
from applications.security.components.mixin_crud import (
    PermissionMixin, ListViewMixin, CreateViewMixin, UpdateViewMixin, DeleteViewMixin
)

class TipoSangreListView(PermissionMixin, ListViewMixin, ListView):
    model = TipoSangre
    template_name = 'core/tiposangre/list.html'
    context_object_name = 'tiposangres'
    permission_required = 'view_tiposangre'

    def get_queryset(self):
        q1 = self.request.GET.get('q')
        if q1:
            self.query.add(Q(tipo__icontains=q1), Q.OR)
            self.query.add(Q(descripcion__icontains=q1), Q.OR)
        return self.model.objects.filter(self.query).order_by('id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('core:tiposangre_create')
        return context
    
    
    
    
    

class TipoSangreCreateView(PermissionMixin, CreateViewMixin, CreateView):
    model = TipoSangre
    form_class = TipoSangreForm
    template_name = 'core/tiposangre/form.html'
    success_url = reverse_lazy('core:tiposangre_list')
    permission_required = 'add_tiposangre'

    def form_valid(self, form):
        messages.success(self.request, 'Tipo de sangre registrado exitosamente.')
        return super().form_valid(form)


class TipoSangreUpdateView(PermissionMixin, UpdateViewMixin, UpdateView):
    model = TipoSangre
    form_class = TipoSangreForm
    template_name = 'core/tiposangre/form.html'
    success_url = reverse_lazy('core:tiposangre_list')
    permission_required = 'change_tiposangre'

    def form_valid(self, form):
        messages.success(self.request, 'Tipo de sangre actualizado correctamente.')
        return super().form_valid(form)


class TipoSangreDeleteView(PermissionMixin, DeleteViewMixin, DeleteView):
    model = TipoSangre
    template_name = 'core/delete.html'
    success_url = reverse_lazy('core:tiposangre_list')
    permission_required = 'delete_tiposangre'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Eliminar Tipo de Sangre'
        context['description'] = f"¿Desea eliminar el tipo de sangre: {self.object}?"
        context['back_url'] = self.success_url
        return context
