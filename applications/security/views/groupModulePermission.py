from django.contrib import messages
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.db.models import Q
from django.contrib.auth.models import Group, Permission
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json

from applications.security.components.mixin_crud import (
    CreateViewMixin, DeleteViewMixin, ListViewMixin, PermissionMixin, UpdateViewMixin
)
from applications.security.forms.groupModulePermission import GroupModulePermissionForm
from applications.security.models import GroupModulePermission, Module

# ---------------------- VISTAS CRUD ---------------------- #

class GroupModulePermissionListView(PermissionMixin, ListViewMixin, ListView):
    template_name = 'security/group_module_permissions/list.html'
    model = Module
    context_object_name = 'modules'
    permission_required = 'view_groupmodulepermission'

    def get_queryset(self):
        q1 = self.request.GET.get('q')
        qs = self.model.objects.prefetch_related(
            'group_permissions__permissions', 'menu'
        ).all()
        if q1:
            qs = qs.filter(group_permissions__group__name__icontains=q1)
        return qs.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('security:group_module_permission_create')
        return context

class GroupModulePermissionCreateView(PermissionMixin, CreateViewMixin, CreateView):
    model = GroupModulePermission
    template_name = 'security/group_module_permissions/form.html'
    form_class = GroupModulePermissionForm
    success_url = reverse_lazy('security:group_module_permission_list')
    permission_required = 'add_groupmodulepermission'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Guardar Permisos'
        context['back_url'] = self.success_url
        context['groups'] = Group.objects.all()
        return context

    def form_valid(self, form):
        messages.success(self.request, "Permisos de grupo registrados con éxito.")
        return super().form_valid(form)

class GroupModulePermissionUpdateView(PermissionMixin, UpdateViewMixin, UpdateView):
    model = GroupModulePermission
    template_name = 'security/group_module_permissions/form.html'
    form_class = GroupModulePermissionForm
    success_url = reverse_lazy('security:group_module_permission_list')
    permission_required = 'change_groupmodulepermission'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Actualizar Permisos'
        context['back_url'] = self.success_url
        context['groups'] = Group.objects.all()  # ✅ Esto es lo que faltaba
        return context

    def form_valid(self, form):
        messages.success(self.request, "Permisos de grupo actualizados con éxito.")
        return super().form_valid(form)


class GroupModulePermissionDeleteView(PermissionMixin, DeleteViewMixin, DeleteView):
    model = GroupModulePermission
    template_name = 'core/delete.html'
    success_url = reverse_lazy('security:group_module_permission_list')
    permission_required = 'delete_groupmodulepermission'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['back_url'] = self.success_url
        context['description'] = f"¿Desea eliminar el grupo {self.object.group.name} del módulo {self.object.module.name}?"
        return context

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Permisos eliminados correctamente.")
        return super().delete(request, *args, **kwargs)

# ---------------------- AJAX ---------------------- #

class GetModulesByGroupView(View):
    def get(self, request, group_id):
        # Se muestran todos los módulos disponibles para que el grupo seleccione
        modules = Module.objects.all()
        data = {
            "modules": [{"id": m.id, "name": m.name} for m in modules]
        }
        return JsonResponse(data)

class GetPermissionsByModuleView(View):
    def get(self, request, module_id):
        try:
            module = Module.objects.get(pk=module_id)
            permissions = module.permissions.all()  # ← Trae solo los permisos asignados al módulo
        except Module.DoesNotExist:
            return JsonResponse({"error": "Módulo no encontrado."}, status=404)

        data = {
            "permissions": [{"id": p.id, "name": p.name} for p in permissions]
        }
        return JsonResponse(data)

@method_decorator(csrf_exempt, name='dispatch')
class SaveGroupPermissionsView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            group_id = data.get('group')
            module_id = data.get('module')
            permission_ids = data.get('permissions', [])

            # Validación
            if not group_id or not module_id or not isinstance(permission_ids, list):
                return JsonResponse({'error': 'Faltan datos o el formato es incorrecto.'}, status=400)

            # ✅ Validar que los IDs existen
            if not Group.objects.filter(id=group_id).exists():
                return JsonResponse({'error': 'El grupo no existe.'}, status=404)
            if not Module.objects.filter(id=module_id).exists():
                return JsonResponse({'error': 'El módulo no existe.'}, status=404)

            # ✅ Validar que los permisos existen (opcional pero útil)
            for pid in permission_ids:
                if not Permission.objects.filter(id=pid).exists():
                    return JsonResponse({'error': f'Permiso ID {pid} no válido.'}, status=400)

            # Eliminar registros anteriores
            GroupModulePermission.objects.filter(group_id=group_id, module_id=module_id).delete()

            # Crear y asignar permisos
            instance = GroupModulePermission.objects.create(
                group_id=group_id,
                module_id=module_id
            )
            instance.permissions.set(permission_ids)

            return JsonResponse({
                "message": "Permisos guardados con éxito.",
                "redirect_url": reverse_lazy('security:group_module_permission_list')
            })

        except Exception as e:
            return JsonResponse({'error': f'Error inesperado: {str(e)}'}, status=500)
