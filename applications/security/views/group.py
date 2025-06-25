from django.contrib import messages
from django.contrib.auth.models import Group
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.db.models import Q

from applications.security.forms.group import GroupForm
from applications.security.components.mixin_crud import (
    PermissionMixin, ListViewMixin, CreateViewMixin, UpdateViewMixin, DeleteViewMixin
)


class GroupListView(PermissionMixin, ListViewMixin, ListView):
    model = Group
    template_name = 'security/groups/list.html'
    context_object_name = 'groups'
    permission_required = 'auth.view_group'

    def get_queryset(self):
        q1 = self.request.GET.get('q')
        if q1:
            self.query.add(Q(name__icontains=q1), Q.OR)
        return self.model.objects.filter(self.query).order_by('id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['create_url'] = reverse_lazy('security:group_create')
        context['title'] = 'Lista de Grupos'
        context['title1'] = 'Grupos'
        return context


class GroupCreateView(PermissionMixin, CreateViewMixin, CreateView):
    model = Group
    template_name = 'security/groups/form.html'
    form_class = GroupForm
    success_url = reverse_lazy('security:group_list')
    permission_required = 'auth.add_group'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Crear Grupo'
        context['title'] = 'Crear Grupo'
        context['title1'] = 'Registrar Grupo'
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        group = self.object
        messages.success(self.request, f"Grupo '{group.name}' creado exitosamente.")
        return response


class GroupUpdateView(PermissionMixin, UpdateViewMixin, UpdateView):
    model = Group
    template_name = 'security/groups/form.html'
    form_class = GroupForm
    success_url = reverse_lazy('security:group_list')
    permission_required = 'auth.change_group'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Actualizar Grupo'
        context['title'] = 'Actualizar Grupo'
        context['title1'] = 'Editar Grupo'
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        group = self.object
        messages.success(self.request, f"Grupo '{group.name}' actualizado correctamente.")
        return response


class GroupDeleteView(PermissionMixin, DeleteViewMixin, DeleteView):
    model = Group
    template_name = 'core/delete.html'
    success_url = reverse_lazy('security:group_list')
    permission_required = 'auth.delete_group'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Eliminar Grupo'
        context['description'] = f"¿Desea eliminar el grupo: {self.object.name}?"
        context['title'] = 'Eliminar Grupo'
        context['title1'] = 'Eliminar Grupo'
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        group_name = self.object.name
        response = super().form_valid(form)
        messages.success(self.request, f"Grupo '{group_name}' eliminado correctamente.")
        return response
