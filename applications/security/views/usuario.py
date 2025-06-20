from django.contrib import messages
from django.urls import reverse_lazy
from applications.security.forms.user import UserForm
from applications.security.components.mixin_crud import CreateViewMixin, DeleteViewMixin, ListViewMixin, PermissionMixin, UpdateViewMixin
from applications.security.forms.menu import MenuForm
from applications.security.forms.module import ModuleForm
from applications.security.models import Menu, Module, User
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.db.models import Q




class UsuarioListView(PermissionMixin, ListViewMixin, ListView):
    template_name = 'security/usuario/list.html'
    model = User
    context_object_name = 'usuarios'
    permission_required = 'view_user'

    def get_queryset(self):
        q1 = self.request.GET.get('q')
        if q1 is not None:
            self.query.add(Q(username__icontains=q1), Q.OR)

        return self.model.objects.filter(self.query).order_by('id')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('security:usuario_create')
        print(context['permissions'])
        return context
    


class UsuarioCreateView(PermissionMixin, CreateViewMixin, CreateView):
    model = User
    template_name = 'security/usuario/form.html'
    form_class = UserForm 
    success_url = reverse_lazy('security:usuario_list')
    permission_required = 'add_user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Grabar Usuario'
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        user = self.object
        messages.success(self.request, f"Éxito al crear el usuario {user.username}.")
        return response
    
class UsuarioUpdateView(PermissionMixin, UpdateViewMixin, UpdateView):
    model = User
    template_name = 'security/usuario/form.html'
    form_class = UserForm
    success_url = reverse_lazy('security:usuario_list')
    permission_required = 'change_user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Actualizar Usuario'
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        user = self.object
        messages.success(self.request, f"Éxito al actualizar el usuario {user.username}.")
        return response

class UsuarioDeleteView(PermissionMixin, DeleteViewMixin, DeleteView):
    model = User
    template_name = 'core/delete.html'
    success_url = reverse_lazy('security:usuario_list')
    permission_required = 'delete_user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        user = self.object
        messages.success(self.request, f"Éxito al eliminar el usuario {user.username}.")
        return response