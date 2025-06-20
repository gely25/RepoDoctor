from django.contrib import messages
from django.urls import reverse_lazy
from applications.security.components.mixin_crud import CreateViewMixin, DeleteViewMixin, ListViewMixin, PermissionMixin, UpdateViewMixin
from applications.security.forms.menu import MenuForm
from applications.security.forms.module import ModuleForm
from applications.security.models import Menu, Module
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.db.models import Q

class GroupModulePermissionListView(PermissionMixin, ListViewMixin, ListView):
    template_name = 'security/group_module_permissions/list.html'
    model = Module
    context_object_name = 'modules'
    permission_required = 'view_groupmodulepermission'

    def get_queryset(self):
        q1 = self.request.GET.get('q')
        if q1 is not None:
            self.query.add(Q(name__icontains=q1), Q.OR)
            self.query.add(Q(menu_name_icontains=q1), Q.OR)
        return self.model.objects.filter(self.query).order_by('id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('security:group_module_permission_create')
        return context

class GroupModulePermissionCreateView(PermissionMixin, CreateViewMixin, CreateView):
    model = Module
    template_name = 'security/group_module_permissions/form.html'
    form_class = ModuleForm
    success_url = reverse_lazy('security:group_module_permission_list')
    permission_required = 'add_groupmodulepermission'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Grabar Grupo de Permisos'
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        module = self.object
        messages.success(self.request, f"Éxito al crear el grupo de permisos {module.name}.")
        return response
    
class GroupModulePermissionUpdateView(PermissionMixin, UpdateViewMixin, UpdateView):
    model = Module
    template_name = 'security/group_module_permissions/form.html'
    form_class = ModuleForm
    success_url = reverse_lazy('security:group_module_permission_list')
    permission_required = 'change_groupmodulepermission'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Actualizar Grupo de Permisos'
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        module = self.object
        messages.success(self.request, f"Éxito al actualizar el grupo de permisos {module.name}.")
        return response
    
class GroupModulePermissionDeleteView(PermissionMixin, DeleteViewMixin, DeleteView):
    model = Module
    template_name = 'security/group_module_permissions/delete.html'
    success_url = reverse_lazy('security:group_module_permission_list')
    permission_required = 'delete_groupmodulepermission'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['back_url'] = self.success_url
        return context

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.success(self.request, "Éxito al eliminar el grupo de permisos.")
        return response
    