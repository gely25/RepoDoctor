from django.contrib import messages
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.db.models import Q
from django.contrib.auth.models import Group, Permission
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
import traceback
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
        context = super().get_context_data(**kwargs)
        context['title'] = 'Asignar Permisos Múltiples'
        context['title1'] = 'Asignar Permisos Múltiples'
        context['grabar'] = 'Guardar Permisos'
        context['back_url'] = self.success_url
        context['groups'] = Group.objects.all().order_by('name')
        context['modules'] = Module.objects.all().order_by('name')
        context['permissions'] = Permission.objects.all()
        context['is_update'] = False

        # --- Agregar configuraciones existentes de todos los grupos ---
        all_permissions = GroupModulePermission.objects.select_related('group', 'module').prefetch_related('permissions')
        existing_configurations = {}

        for gmp in all_permissions:
            group_id = gmp.group.id
            module_id = gmp.module.id

            if group_id not in existing_configurations:
                existing_configurations[group_id] = {
                    'group_id': group_id,
                    'group_name': gmp.group.name,
                    'modules': [],
                    'permissions': {}
                }

            if module_id not in existing_configurations[group_id]['modules']:
                existing_configurations[group_id]['modules'].append(module_id)

            existing_configurations[group_id]['permissions'][module_id] = list(
                gmp.permissions.values_list('id', flat=True)
            )

        import json
        context['existing_configurations'] = json.dumps(existing_configurations)
        return context




class GroupModulePermissionUpdateView(PermissionMixin, UpdateViewMixin, UpdateView):
    model = GroupModulePermission
    template_name = 'security/group_module_permissions/form.html'
    form_class = GroupModulePermissionForm
    success_url = reverse_lazy('security:group_module_permission_list')
    permission_required = 'change_groupmodulepermission'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Permisos de Grupo'
        context['title1'] = 'Editar Permisos de Grupo'
        context['grabar'] = 'Actualizar Permisos'
        context['back_url'] = self.success_url
        context['groups'] = Group.objects.all().order_by('name')
        context['is_update'] = True
        
        # Obtener el objeto actual
        obj = self.get_object()
        
        # Datos básicos del objeto actual
        context['existing_data'] = {
            'group_id': obj.group.id,
            'group_name': obj.group.name,
            'module_id': obj.module.id,
            'module_name': obj.module.name,
            'permission_ids': list(obj.permissions.values_list('id', flat=True))
        }
        
        # Configuración completa del grupo
        existing_configurations = {}
        
        # Obtener TODAS las configuraciones existentes del grupo actual
        group_permissions = GroupModulePermission.objects.filter(
            group=obj.group
        ).prefetch_related('permissions', 'module')
        
        if group_permissions.exists():
            group_config = {
                'group_id': obj.group.id,
                'group_name': obj.group.name,
                'modules': [],
                'permissions': {}
            }
            
            for perm_obj in group_permissions:
                module_id = perm_obj.module.id
                
                # Agregar módulo si no está en la lista
                if module_id not in group_config['modules']:
                    group_config['modules'].append(module_id)
                
                # Agregar permisos del módulo
                group_config['permissions'][module_id] = list(
                    perm_obj.permissions.values_list('id', flat=True)
                )
            
            existing_configurations[obj.group.id] = group_config
        
        # Convertir a JSON seguro para JavaScript
        import json
        context['existing_configurations'] = json.dumps(existing_configurations)
        context['existing_data'] = json.dumps(context['existing_data'])
        
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
        context = super().get_context_data(**kwargs)
        context['back_url'] = self.success_url
        context['description'] = f"¿Desea eliminar el grupo {self.object.group.name} del módulo {self.object.module.name}?"
        return context

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Permisos eliminados correctamente.")
        return super().delete(request, *args, **kwargs)

# ---------------------- VISTA ADICIONAL PARA OBTENER TODOS LOS PERMISOS ---------------------- #

class GetAllModulePermissionsView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            module_ids = data.get('module_ids', [])

            if not module_ids:
                return JsonResponse({
                    'success': False,
                    'message': 'No se proporcionaron IDs de módulos'
                }, status=400)

            modules_data = {}
            for module_id in module_ids:
                try:
                    module = Module.objects.get(pk=module_id)
                    permissions = module.permissions.all().order_by('name')

                    modules_data[str(module_id)] = {
                        'name': module.name,
                        'permissions': [
                            {'id': p.id, 'name': p.name, 'codename': p.codename}
                            for p in permissions
                        ]
                    }
                except Module.DoesNotExist:
                    continue

            return JsonResponse({
                'success': True,
                'modules': modules_data
            })

        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'message': 'Formato inválido'}, status=400)
        except Exception as e:
            return JsonResponse({'success': False, 'message': f'Error: {str(e)}'}, status=500)



@method_decorator(csrf_exempt, name='dispatch')
class SaveMultipleGroupPermissionsView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            selections = data.get('selections', [])
            is_update = data.get('is_update', False)

            if not selections:
                return JsonResponse({
                    'success': False,
                    'message': 'No se recibieron configuraciones para guardar.'
                }, status=400)

            grouped_data = {}
            for item in selections:
                group_id = item.get('group_id')
                grouped_data.setdefault(group_id, []).append(item)

            total_saved = 0
            total_skipped = 0
            errors = []

            for group_id, items in grouped_data.items():
                try:
                    group = Group.objects.get(pk=group_id)
                except Group.DoesNotExist:
                    errors.append(f"Grupo ID {group_id} no encontrado.")
                    continue

                existentes = GroupModulePermission.objects.filter(group=group)
                actuales = {obj.module_id: obj for obj in existentes}

                modulos_procesados = set()

                for item in items:
                    module_id = item.get('module_id')
                    permission_ids = item.get('permission_ids', [])

                    if not permission_ids:
                        continue

                    try:
                        module = Module.objects.get(pk=module_id)
                        permisos = Permission.objects.filter(id__in=permission_ids)
                    except Module.DoesNotExist:
                        errors.append(f"Módulo ID {module_id} no encontrado.")
                        continue

                    if module_id in actuales:
                        if is_update:
                            gmp = actuales[module_id]
                            gmp.permissions.set(permisos)
                            gmp.save()
                        else:
                            # En modo creación no se sobreescribe lo ya existente
                            total_skipped += 1
                            continue
                    else:
                        gmp = GroupModulePermission.objects.create(group=group, module=module)
                        gmp.permissions.set(permisos)
                        total_saved += 1

                    modulos_procesados.add(module_id)

                # Solo si estamos actualizando eliminamos módulos no enviados
                if is_update:
                    for mod_id, obj in actuales.items():
                        if mod_id not in modulos_procesados:
                            obj.delete()

            return JsonResponse({
                'success': True,
                'message': f"Guardado exitoso. Nuevos: {total_saved}, Omitidos: {total_skipped}",
                'redirect_url': str(reverse_lazy('security:group_module_permission_list')),
                'errors': errors
            })

        except json.JSONDecodeError:
            return JsonResponse({
                'success': False,
                'message': 'Formato de datos inválido.'
            }, status=400)
       

        except Exception as e:
            print("ERROR GUARDANDO PERMISOS:")
            traceback.print_exc()
            return JsonResponse({
                'success': False,
                'message': f'Error inesperado: {str(e)}'
            }, status=500)




class GetModulesByGroupView(View):
    def get(self, request, group_id):
        try:
            modules = Module.objects.all().order_by('name')

            data = {
                "modules": [
                    {
                        "id": m.id,
                        "name": m.name,
                        "permissions_count": m.permissions.count()
                    }
                    for m in modules
                ]
            }
            return JsonResponse(data)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)


class GetPermissionsByModuleView(View):
    def get(self, request, module_id):
        try:
            module = Module.objects.get(pk=module_id)
            permissions = module.permissions.all().order_by('name')

            data = {
                "permissions": [
                    {"id": p.id, "name": p.name, "codename": p.codename}
                    for p in permissions
                ]
            }
            return JsonResponse(data)
        except Module.DoesNotExist:
            return JsonResponse({"error": "Módulo no encontrado"}, status=404)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)




















# from django.contrib import messages
# from django.http import JsonResponse
# from django.urls import reverse_lazy
# from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
# from django.db.models import Q
# from django.contrib.auth.models import Group, Permission
# from django.views.decorators.csrf import csrf_exempt
# from django.utils.decorators import method_decorator
# import json

# from applications.security.components.mixin_crud import (
#     CreateViewMixin, DeleteViewMixin, ListViewMixin, PermissionMixin, UpdateViewMixin
# )
# from applications.security.forms.groupModulePermission import GroupModulePermissionForm
# from applications.security.models import GroupModulePermission, Module

# # ---------------------- VISTAS CRUD ---------------------- #

# class GroupModulePermissionListView(PermissionMixin, ListViewMixin, ListView):
#     template_name = 'security/group_module_permissions/list.html'
#     model = Module
#     context_object_name = 'modules'
#     permission_required = 'view_groupmodulepermission'

#     def get_queryset(self):
#         q1 = self.request.GET.get('q')
#         qs = self.model.objects.prefetch_related(
#             'group_permissions__permissions', 'menu'
#         ).all()
#         if q1:
#             qs = qs.filter(group_permissions__group__name__icontains=q1)
#         return qs.distinct()

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['create_url'] = reverse_lazy('security:group_module_permission_create')
#         return context


# class GroupModulePermissionCreateView(PermissionMixin, CreateViewMixin, CreateView):
#     model = GroupModulePermission
#     template_name = 'security/group_module_permissions/form.html'  # ← si estás usando form_multi.html, cambia esto
#     form_class = GroupModulePermissionForm
#     success_url = reverse_lazy('security:group_module_permission_list')
#     permission_required = 'add_groupmodulepermission'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['grabar'] = 'Guardar Permisos'
#         context['back_url'] = self.success_url
#         context['groups'] = Group.objects.all()
#         context['modules'] = Module.objects.all() 
#         return context

#     def form_valid(self, form):
#         messages.success(self.request, "Permisos de grupo registrados con éxito.")
#         return super().form_valid(form)






# class GroupModulePermissionUpdateView(PermissionMixin, UpdateViewMixin, UpdateView):
#     model = GroupModulePermission
#     template_name = 'security/group_module_permissions/form.html'
#     form_class = GroupModulePermissionForm
#     success_url = reverse_lazy('security:group_module_permission_list')
#     permission_required = 'change_groupmodulepermission'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data()
#         context['grabar'] = 'Actualizar Permisos'
#         context['back_url'] = self.success_url
#         context['groups'] = Group.objects.all()
#         return context

#     def form_valid(self, form):
#         messages.success(self.request, "Permisos de grupo actualizados con éxito.")
#         return super().form_valid(form)


# class GroupModulePermissionDeleteView(PermissionMixin, DeleteViewMixin, DeleteView):
#     model = GroupModulePermission
#     template_name = 'core/delete.html'
#     success_url = reverse_lazy('security:group_module_permission_list')
#     permission_required = 'delete_groupmodulepermission'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data()
#         context['back_url'] = self.success_url
#         context['description'] = f"¿Desea eliminar el grupo {self.object.group.name} del módulo {self.object.module.name}?"
#         return context

#     def delete(self, request, *args, **kwargs):
#         messages.success(self.request, "Permisos eliminados correctamente.")
#         return super().delete(request, *args, **kwargs)

# # ---------------------- AJAX ---------------------- #

# class GetModulesByGroupView(View):
#     def get(self, request, group_id):
#         # Se muestran todos los módulos disponibles para que el grupo seleccione
#         modules = Module.objects.all()
#         data = {
#             "modules": [{"id": m.id, "name": m.name} for m in modules]
#         }
#         return JsonResponse(data)

# class GetPermissionsByModuleView(View):
#     def get(self, request, module_id):
#         try:
#             module = Module.objects.get(pk=module_id)
#             permissions = module.permissions.all()  # ← Trae solo los permisos asignados al módulo
#         except Module.DoesNotExist:
#             return JsonResponse({"error": "Módulo no encontrado."}, status=404)

#         data = {
#             "permissions": [{"id": p.id, "name": p.name} for p in permissions]
#         }
#         return JsonResponse(data)
    
    


# @method_decorator(csrf_exempt, name='dispatch')
# class SaveGroupPermissionsMultiView(View):
#     def post(self, request):
#         try:
#             data = json.loads(request.body)

#             if not isinstance(data, dict) or not data:
#                 return JsonResponse({'error': 'Datos inválidos recibidos.'}, status=400)

#             for group_id, modules in data.items():
#                 if not Group.objects.filter(id=group_id).exists():
#                     continue
#                 for module_id, permission_ids in modules.items():
#                     if not Module.objects.filter(id=module_id).exists():
#                         continue

#                     # Filtrar permisos válidos
#                     valid_permission_ids = Permission.objects.filter(id__in=permission_ids).values_list('id', flat=True)

#                     # Eliminar asignaciones previas para este grupo-módulo
#                     GroupModulePermission.objects.filter(group_id=group_id, module_id=module_id).delete()

#                     # Crear nueva asignación
#                     instance = GroupModulePermission.objects.create(
#                         group_id=group_id,
#                         module_id=module_id
#                     )
#                     instance.permissions.set(valid_permission_ids)

#             return JsonResponse({
#                 'message': 'Permisos guardados con éxito.',
#                 'redirect_url': reverse_lazy('security:group_module_permission_list')
#             })

#         except Exception as e:
#             return JsonResponse({'error': f'Error inesperado: {str(e)}'}, status=500)


