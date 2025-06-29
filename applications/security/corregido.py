from django.db import models
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from applications.security.models import GroupModulePermission, Menu, Module, User
# ============================================================================
# CREACIÓN DE MENÚS
# ============================================================================

# Create Menus - using save() and create()
menu1 = Menu(
    name='Registros',
    icon='fas fa-user-plus',
    order=1
)
menu1.save()

menu2 = Menu(
    name='Emergencia',
    icon='fas fa-ambulance',
    order=2
)
menu2.save()

menu3 = Menu.objects.create(
    name='Consultas',
    icon='fas fa-stethoscope',
    order=3
)

menu4 = Menu.objects.create(
    name='Auditores',
    icon='fas fa-user-shield',
    order=4
)

# Menú Seguridad con get_or_create
menu5, created = Menu.objects.get_or_create(
    name='Seguridad',
    defaults={'icon': 'bi bi-shield-lock', 'order': 5}
)


# Menú Gestión Médica con get_or_create
menu6, created = Menu.objects.get_or_create(
    name='Gestión Médica',
    defaults={'icon': 'bi bi-shield-lock', 'order': 6}
    
)




# ============================================================================
# CREACIÓN DE MÓDULOS
# ============================================================================

# Create Modules using bulk_create
modules = [
    # Modules for Registros menu
    Module(url='pacientes/', name='Registro de Pacientes', menu_id=menu1.id,
           description='Gestión de información de pacientes', icon='fas fa-user-plus', order=1),
    Module(url='historial/', name='Historial Médico', menu=menu1,
           description='Historial clínico de pacientes', icon='fas fa-file-medical', order=2),
    Module(url='seguimiento/', name='Seguimiento', menu=menu1,
           description='Seguimiento de tratamientos y evolución', icon='fas fa-chart-line', order=3),

    # Modules for Emergencia menu
    Module(url='citas/', name='Citas', menu=menu2,
           description='Programación de citas médicas', icon='fas fa-calendar-alt', order=1),
    Module(url='diagnosticos/', name='Diagnósticos', menu=menu2,
           description='Registro de diagnósticos médicos', icon='fas fa-diagnoses', order=2),
    Module(url='recetas/', name='Recetas', menu=menu2,
           description='Emisión de recetas médicas', icon='fas fa-prescription-bottle-alt', order=3),

    # Modules for Consultas menu
    Module(url='usuarios/', name='Usuarios', menu=menu3,
           description='Gestión de usuarios del sistema', icon='fas fa-users', order=1),
    Module(url='configuracion/', name='Configuración', menu=menu3,
           description='Configuración general del sistema', icon='fas fa-cogs', order=2),
    Module(url='reportes/', name='Reportes', menu=menu3,
           description='Generación de reportes y estadísticas', icon='fas fa-chart-bar', order=3),
    

]
created_modules = Module.objects.bulk_create(modules)
module1, module2, module3, module4, module5, module6, module7, module8, module9 = created_modules

# Módulos adicionales para Seguridad con get_or_create
module10, created = Module.objects.get_or_create(
    url='security/menu_list/',
    name='Menus',
    menu=menu5,
    defaults={
        'description': 'Administración de menús',
        'icon': 'fas fa-bars',
        'order': 1
    }
)

module11, created = Module.objects.get_or_create(
    url='security/module_list/',
    name='Módulos',
    menu=menu5,
    defaults={
        'description': 'Administración de módulos',
        'icon': 'fas fa-cubes',
        'order': 2
    }
)
module12, created = Module.objects.get_or_create(
    url='security/usuario_list/',
    name='Usuarios',
    menu=menu5,
    defaults={
        'description': 'Administración de usuarios del sistema',
        'icon': 'fas fa-user-shield',
        'order': 3
    }
)
module13, created = Module.objects.get_or_create(
    url='security/group_module_permission_list/',
    name='Grupos de Permisos',
    menu=menu5,
    defaults={
        'description': 'Administración de grupos de permisos',
        'icon': 'fas fa-users-cog',
        'order': 4
    }
)




# Módulos adicionales para Gestión Médica con get_or_create
module14, created = Module.objects.get_or_create(
    url='core/cargo_list/',
    name='Cargos',
    menu=menu6,
    defaults={
        'description': 'Administración de Cargos',
        'icon': 'fas fa-bars',
        'order': 1
    }
)

module15, created = Module.objects.get_or_create(
    url='core/especialidad_list/',
    name='Módulos',
    menu=menu6,
    defaults={
        'description': 'Administración de Especialidades',
        'icon': 'fas fa-cubes',
        'order': 2
    }
)
module16, created = Module.objects.get_or_create(
    url='security/doctor_list/',
    name='Doctores',
    menu=menu6,
    defaults={
        'description': 'Administración de Doctores',
        'icon': 'fas fa-user-shield',
        'order': 3
    }
)
module17, created = Module.objects.get_or_create(
    url='security/empleado_list/',
    name='Empleados',
    menu=menu6,
    defaults={
        'description': 'Administración de Empleados',
        'icon': 'fas fa-users-cog',
        'order': 4
    }
)






# ============================================================================
# CREACIÓN DE USUARIOS
# ============================================================================

# Create Users
user1 = User.objects.create_user(
    username='drgomez2',
    email='drgomezz@clinica.med',
    password='secure123!',
    first_name='Carlos',
    last_name='Gómez',
    dni='0912345678',
    direction='Av. Principal 123, Guayaquil',
    phone='0991234567',
    is_staff=True
)

user2 = User.objects.create_user(
    username='asistente',
    email='asistente@clinica.med',
    password='asist2025!',
    first_name='María',
    last_name='Sánchez',
    dni='0923456789',
    direction='Calle Secundaria 456, Guayaquil',
    phone='0982345678',
    is_staff=False
)

# ============================================================================
# CREACIÓN DE GRUPOS
# ============================================================================

# Create Groups
group_medicos = Group.objects.create(name='Médicos')
group_asistentes = Group.objects.create(name='Asistentes')

# Add users to groups
user1.groups.add(group_medicos) 
user2.groups.add(group_asistentes)

# ============================================================================
# CREACIÓN DE PERMISOS
# ============================================================================

# Create permissions for Patient and Diagnosis models
# patient_ct = ContentType.objects.get(app_label='doctor', model='patient')
# diagnosis_ct = ContentType.objects.get(app_label='doctor', model='diagnosis')
# Patient permissions
patient_view = Permission.objects.get_or_create(codename='view_patient', name='Can view Paciente', content_type=patient_ct)[0]
patient_add = Permission.objects.get_or_create(codename='add_patient', name='Can add Paciente', content_type=patient_ct)[0]
patient_change = Permission.objects.get_or_create(codename='change_patient', name='Can change Paciente', content_type=patient_ct)[0]
patient_delete = Permission.objects.get_or_create(codename='delete_patient', name='Can delete Paciente', content_type=patient_ct)[0]

# Diagnosis permissions
diagnosis_view = Permission.objects.get_or_create(codename='view_diagnosis', name='Can view Diagnóstico', content_type=diagnosis_ct)[0]
diagnosis_add = Permission.objects.get_or_create(codename='add_diagnosis', name='Can add Diagnóstico', content_type=diagnosis_ct)[0]
diagnosis_change = Permission.objects.get_or_create(codename='change_diagnosis', name='Can change Diagnóstico', content_type=diagnosis_ct)[0]
diagnosis_delete = Permission.objects.get_or_create(codename='delete_diagnosis', name='Can delete Diagnóstico', content_type=diagnosis_ct)[0]


# ============================================================================
# CREACIÓN DE PERMISOS - SECCIÓN CORREGIDA
# ============================================================================

# ContentTypes para los modelos de seguridad
menu_ct = ContentType.objects.get(app_label='security', model='menu')
module_ct = ContentType.objects.get(app_label='security', model='module')
user_ct = ContentType.objects.get(app_label='security', model='user')  # Cambié usuario_ct por user_ct
group_module_permission_ct = ContentType.objects.get(app_label='security', model='groupmodulepermission')



#contentTypes para modelos de Gestion médica

cargo_ct= ContentType.objects.get(app_label= 'core', model= 'cargo')
especialidad_ct= ContentType.objects.get(app_label= 'core', model= 'especialidadmedica')
doctor_ct= ContentType.objects.get(app_label= 'core', model= 'doctor')
empleado_ct= ContentType.objects.get(app_label= 'core', model= 'empleado')
tiposangre_ct= ContentType.objects.get(app_label= 'core', model= 'tiposangre')
paciente_ct= ContentType.objects.get(app_label= 'core', model= 'paciente')
marcamedicamento_ct= ContentType.objects.get(app_label= 'core', model= 'marcamedicamento')
tipomedicamento_ct= ContentType.objects.get(app_label= 'core', model= 'tipomedicamento')
medicamento_ct= ContentType.objects.get(app_label= 'core', model= 'medicamento')
tipogasto_ct= ContentType.objects.get(app_label= 'core', model= 'tipogasto')
gastomensual_ct= ContentType.objects.get(app_label= 'core', model= 'gastomensual')
diagnostico_ct=ContentType.objects.get(app_label= 'core', model= 'diagnostico')
fotopaciente_ct=ContentType.objects.get(app_label= 'core', model= 'fotopaciente')

# Permisos de Menu
menu_view = Permission.objects.get_or_create(
    codename='view_menu',
    content_type=menu_ct,
    defaults={'name': 'Can view Menu'}
)[0]
menu_add = Permission.objects.get_or_create(
    codename='add_menu',
    content_type=menu_ct,
    defaults={'name': 'Can add Menu'}
)[0]
menu_change = Permission.objects.get_or_create(
    codename='change_menu',
    content_type=menu_ct,
    defaults={'name': 'Can change Menu'}
)[0]
menu_delete = Permission.objects.get_or_create(
    codename='delete_menu',
    content_type=menu_ct,
    defaults={'name': 'Can delete Menu'}
)[0]

# Permisos de Module
module_view = Permission.objects.get_or_create(
    codename='view_module',
    content_type=module_ct,
    defaults={'name': 'Can view Module'}
)[0]
module_add = Permission.objects.get_or_create(
    codename='add_module',
    content_type=module_ct,
    defaults={'name': 'Can add Module'}
)[0]
module_change = Permission.objects.get_or_create(
    codename='change_module',
    content_type=module_ct,
    defaults={'name': 'Can change Module'}
)[0]
module_delete = Permission.objects.get_or_create(
    codename='delete_module',
    content_type=module_ct,
    defaults={'name': 'Can delete Module'}
)[0]

# Permisos de User - CORREGIDO
user_view = Permission.objects.get_or_create(  # Cambié module_view por user_view
    codename='view_user',
    content_type=user_ct,  # Cambié usuario_ct por user_ct
    defaults={'name': 'Can view User'}
)[0]
user_add = Permission.objects.get_or_create(  # Cambié usuario_add por user_add
    codename='add_user',
    content_type=user_ct,
    defaults={'name': 'Can add User'}
)[0]
user_change = Permission.objects.get_or_create(  # Cambié usuario_change por user_change
    codename='change_user',
    content_type=user_ct,
    defaults={'name': 'Can change User'}
)[0]
user_delete = Permission.objects.get_or_create(  # Cambié usuario_delete por user_delete
    codename='delete_user',
    content_type=user_ct,
    defaults={'name': 'Can delete User'}
)[0]
# Permisos de GroupModulePermission
group_module_permission_view = Permission.objects.get_or_create(
    codename='view_groupmodulepermission',
    content_type=group_module_permission_ct,
    defaults={'name': 'Can view GroupModulePermission'}
)[0]
group_module_permission_add = Permission.objects.get_or_create(
    codename='add_groupmodulepermission',
    content_type=group_module_permission_ct,
    defaults={'name': 'Can add GroupModulePermission'}
)[0]
group_module_permission_change = Permission.objects.get_or_create(
    codename='change_groupmodulepermission',
    content_type=group_module_permission_ct,
    defaults={'name': 'Can change GroupModulePermission'}
)[0]
group_module_permission_delete = Permission.objects.get_or_create(
    codename='delete_groupmodulepermission',
    content_type=group_module_permission_ct,
    defaults={'name': 'Can delete GroupModulePermission'}
)[0]



# Permisos de GroupModulePermission
group_module_permission_view = Permission.objects.get_or_create(
    codename='view_groupmodulepermission',
    content_type=group_module_permission_ct,
    defaults={'name': 'Can view GroupModulePermission'}
)[0]
group_module_permission_add = Permission.objects.get_or_create(
    codename='add_groupmodulepermission',
    content_type=group_module_permission_ct,
    defaults={'name': 'Can add GroupModulePermission'}
)[0]
group_module_permission_change = Permission.objects.get_or_create(
    codename='change_groupmodulepermission',
    content_type=group_module_permission_ct,
    defaults={'name': 'Can change GroupModulePermission'}
)[0]
group_module_permission_delete = Permission.objects.get_or_create(
    codename='delete_groupmodulepermission',
    content_type=group_module_permission_ct,
    defaults={'name': 'Can delete GroupModulePermission'}
)[0]




########## CREACIÓN DE PERMISOS: GESTIÓN SEGURIDAD

# Permisos de Cargo - CORREGIDO
cargo_view = Permission.objects.get_or_create(  
    codename='view_cargo',
    content_type=cargo_ct,
    defaults={'name': 'Can view cargo'}
)[0]
cargo_add = Permission.objects.get_or_create(  # Cambié usuario_add por user_add
    codename='add_cargo',
    content_type=cargo_ct,
    defaults={'name': 'Can add cargo'}
)[0]
cargo_change = Permission.objects.get_or_create(  # Cambié usuario_change por user_change
    codename='change_cargo',
    content_type=cargo_ct,
    defaults={'name': 'Can change cargo'}
)[0]
cargo_delete = Permission.objects.get_or_create(  # Cambié usuario_delete por user_delete
    codename='delete_cargo',
    content_type=cargo_ct,
    defaults={'name': 'Can delete cargo'}
)[0]




# Permisos de Especialidad- CORREGIDO
especialidadmedica_view= Permission.objects.get_or_create(  
    codename='view_especialidadmedica',
    content_type=especialidad_ct,
    defaults={'name': 'Can view especialidad medica'}
)[0]

especialidadmedica_add= Permission.objects.get_or_create(  
    codename='add_especialidadmedica',
    content_type=especialidad_ct,
    defaults={'name': 'Can add especialidad medica'}
)[0]

especialidadmedica_change= Permission.objects.get_or_create(  
    codename='change_especialidadmedica',
    content_type=especialidad_ct,
    defaults={'name': 'Can change especialidad medica'}
)[0]

especialidadmedica_delete= Permission.objects.get_or_create(  
    codename='delete_especialidadmedica',
    content_type=especialidad_ct,
    defaults={'name': 'Can delete especialidad medica'}
)[0]



# Permisos de Doctores - CORREGIDO
doctor_view= Permission.objects.get_or_create(  
    codename='view_doctor',
    content_type=doctor_ct,
    defaults={'name': 'Can view doctor'}
)[0]


doctor_add= Permission.objects.get_or_create(  
    codename='add_doctor',
    content_type=doctor_ct,
    defaults={'name': 'Can add doctor'}
)[0]

doctor_change= Permission.objects.get_or_create(  
    codename='change_doctor',
    content_type=doctor_ct,
    defaults={'name': 'Can change doctor'}
)[0]


doctor_delete= Permission.objects.get_or_create(  
    codename='delete_doctor',
    content_type=doctor_ct,
    defaults={'name': 'Can delete doctor'}
)[0]



# Permisos de Empleados - CORREGIDO
empleado_view= Permission.objects.get_or_create(  
    codename='view_empleado',
    content_type=empleado_ct,
    defaults={'name': 'Can view empleado'}
)[0]

empleado_add= Permission.objects.get_or_create(  
    codename='add_empleado',
    content_type=empleado_ct,
    defaults={'name': 'Can add empleado'}
)[0]

empleado_change= Permission.objects.get_or_create(  
    codename='change_empleado',
    content_type=empleado_ct,
    defaults={'name': 'Can change empleado'}
)[0]


empleado_delete= Permission.objects.get_or_create(  
    codename='delete_empleado',
    content_type=empleado_ct,
    defaults={'name': 'Can delete empleado'}
)[0]





# ============================================================================
# CREACIÓN DE GroupModulePermission - VERSIÓN OPTIMIZADA
# ============================================================================

# Crear todas las relaciones usando get_or_create para evitar duplicados
# Médicos - Módulos principales
gmp_medicos_pacientes, created = GroupModulePermission.objects.get_or_create(
    group=group_medicos, 
    module=module1
)
if created:
    gmp_medicos_pacientes.permissions.add(patient_view, patient_add, patient_change, patient_delete)

gmp_medicos_diagnosticos, created = GroupModulePermission.objects.get_or_create(
    group=group_medicos, 
    module=module5
)
if created:
    gmp_medicos_diagnosticos.permissions.add(diagnosis_view, diagnosis_add, diagnosis_change)

# Médicos - Módulos adicionales
gmp_medicos_historial, created = GroupModulePermission.objects.get_or_create(
    group=group_medicos, 
    module=module2
)
gmp_medicos_seguimiento, created = GroupModulePermission.objects.get_or_create(
    group=group_medicos, 
    module=module3
)
gmp_medicos_recetas, created = GroupModulePermission.objects.get_or_create(
    group=group_medicos, 
    module=module6
)

# Asistentes - Módulos con permisos limitados
gmp_asist_pacientes, created = GroupModulePermission.objects.get_or_create(
    group=group_asistentes, 
    module=module1
)
if created:
    gmp_asist_pacientes.permissions.add(patient_view, patient_add)

gmp_asist_citas, created = GroupModulePermission.objects.get_or_create(
    group=group_asistentes, 
    module=module4
)

gmp_asist_diagnosticos, created = GroupModulePermission.objects.get_or_create(
    group=group_asistentes, 
    module=module5
)
if created:
    gmp_asist_diagnosticos.permissions.add(diagnosis_view)

# Asistentes - Módulos de Seguridad
gmp_asist_menu, created = GroupModulePermission.objects.get_or_create(
    group=group_asistentes, 
    module=module10
)
if created:
    gmp_asist_menu.permissions.set([menu_view, menu_add, menu_change, menu_delete])

gmp_asist_module, created = GroupModulePermission.objects.get_or_create(
    group=group_asistentes, 
    module=module11
)
if created:
    gmp_asist_module.permissions.set([module_view, module_add, module_change, module_delete])

gmp_asist_user, created = GroupModulePermission.objects.get_or_create(
    group=group_asistentes, 
    module=module12
)
if created:
    gmp_asist_user.permissions.set([user_view, user_add, user_change, user_delete])  # Usando las variables corregidas

gmp_asist_group_module_permission, created = GroupModulePermission.objects.get_or_create(
    group=group_asistentes,
    module=module13
)
if created:
    gmp_asist_group_module_permission.permissions.set([
        group_module_permission_view, 
        group_module_permission_add, 
        group_module_permission_change, 
        group_module_permission_delete
    ])
    
    
    
    
    
    
    
# Asignar los módulos de Gestión Médica solo a los Asistentes 

gmp_asist_cargos, created=GroupModulePermission.objects.get_or_create(
    group=group_asistentes,
    module=module14  # Cargos
)
if created:
    gmp_asist_cargos.permissions.set([cargo_view])

gmp_asist_especialidad, _= GroupModulePermission.objects.get_or_create(
    group=group_asistentes,
    module=module15  # Especialidades
)

gmp_asist_especialidad.permissions.set([especialidadmedica_view, especialidadmedica_add, especialidadmedica_change, especialidadmedica_change])


gmp_asist_doctores, _= GroupModulePermission.objects.get_or_create(
    group=group_asistentes,
    module=module16  # Doctores
)

gmp_asist_doctores.permissions.set([doctor_add, doctor_delete, doctor_view, doctor_change])

gmp_asist_empleados,_=GroupModulePermission.objects.get_or_create(
    group=group_asistentes,
    module=module17  # Empleados
)
gmp_asist_empleados.permissions.set([empleado_add, empleado_change, empleado_view, empleado_delete])




