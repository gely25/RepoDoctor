from django.db import models
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from applications.security.models import GroupModulePermission, Menu, Module, User

# ============================================================================
# CREACIÓN DE MENÚS
# ============================================================================



menu1, created= Menu.objects.get_or_create(
    name='Registros', 
    defaults={'icon': 'bi bi-person', 'order': 1}
    )

menu2, _ = Menu.objects.get_or_create(
    name='Emergencia',
    defaults={'icon': 'fas fa-ambulance', 'order': 2}
)

menu3, _ = Menu.objects.get_or_create(
    name='Consultas',
    defaults={'icon': 'fas fa-stethoscope', 'order': 3}
)

menu4, _ = Menu.objects.get_or_create(
    name='Auditores',
    defaults={'icon': 'fas fa-user-shield', 'order': 4}
)

menu5, _ = Menu.objects.get_or_create(
    name='Seguridad',
    defaults={'icon': 'bi bi-shield-lock', 'order': 5}
)

menu6, _ = Menu.objects.get_or_create(
    name='Gestión Médica',
    defaults={'icon': 'bi bi-shield-lock', 'order': 6}
)


# ============================================================================
# CREACIÓN DE MÓDULOS
# ============================================================================


def crear_modulo(url, name, menu, description, icon, order):
    module, _ = Module.objects.get_or_create(
        url=url,
        name=name,
        menu=menu,
        defaults={
            'description': description,
            'icon': icon,
            'order': order
        }
    )
    return module


# === Módulos para el menú Registros ===
module1 = crear_modulo(
    url='pacientes/',
    name='Registro de Pacientes',
    menu=menu1,
    description='Gestión de información de pacientes',
    icon='fas fa-user-plus',
    order=1
)

module2 = crear_modulo(
    url='historial/',
    name='Historial Médico',
    menu=menu1,
    description='Historial clínico de pacientes',
    icon='fas fa-file-medical',
    order=2
)

module3 = crear_modulo(
    url='seguimiento/',
    name='Seguimiento',
    menu=menu1,
    description='Seguimiento de tratamientos y evolución',
    icon='fas fa-chart-line',
    order=3
)

# === Módulos para el menú Emergencia ===
module4 = crear_modulo(
    url='citas/',
    name='Citas',
    menu=menu2,
    description='Programación de citas médicas',
    icon='fas fa-calendar-alt',
    order=1
)

module5 = crear_modulo(
    url='diagnosticos/',
    name='Diagnósticos',
    menu=menu2,
    description='Registro de diagnósticos médicos',
    icon='fas fa-diagnoses',
    order=2
)

module6 = crear_modulo(
    url='recetas/',
    name='Recetas',
    menu=menu2,
    description='Emisión de recetas médicas',
    icon='fas fa-prescription-bottle-alt',
    order=3
)

# === Módulos para el menú Consultas ===
module7 = crear_modulo(
    url='usuarios/',
    name='Usuarios',
    menu=menu3,
    description='Gestión de usuarios del sistema',
    icon='fas fa-users',
    order=1
)

module8 = crear_modulo(
    url='configuracion/',
    name='Configuración',
    menu=menu3,
    description='Configuración general del sistema',
    icon='fas fa-cogs',
    order=2
)

module9 = crear_modulo(
    url='reportes/',
    name='Reportes',
    menu=menu3,
    description='Generación de reportes y estadísticas',
    icon='fas fa-chart-bar',
    order=3
)

# === Módulos para el menú Seguridad ===
module10 = crear_modulo(
    url='security/menu_list/',
    name='Menus',
    menu=menu5,
    description='Administración de menús',
    icon='fas fa-bars',
    order=1
)

module11 = crear_modulo(
    url='security/module_list/',
    name='Módulos',
    menu=menu5,
    description='Administración de módulos',
    icon='fas fa-cubes',
    order=2
)

module12 = crear_modulo(
    url='security/usuario_list/',
    name='Usuarios',
    menu=menu5,
    description='Administración de usuarios del sistema',
    icon='fas fa-user-shield',
    order=3
)

module13 = crear_modulo(
    url='security/group_module_permission_list/',
    name='Grupos de Permisos',
    menu=menu5,
    description='Administración de grupos de permisos',
    icon='fas fa-users-cog',
    order=4
)

# === Módulos para el menú Gestión Médica ===
module14 = crear_modulo(
    url='core/cargo_list/',
    name='Cargos',
    menu=menu6,
    description='Administración de Cargos',
    icon='fas fa-bars',
    order=1
)

module15 = crear_modulo(
    url='core/especialidad_list/',
    name='Especialidades',
    menu=menu6,
    description='Administración de Especialidades',
    icon='fas fa-cubes',
    order=2
)

module16 = crear_modulo(
    url='security/doctor_list/',
    name='Doctores',
    menu=menu6,
    description='Administración de Doctores',
    icon='fas fa-user-shield',
    order=3
)

module17 = crear_modulo(
    url='security/empleado_list/',
    name='Empleados',
    menu=menu6,
    description='Administración de Empleados',
    icon='fas fa-users-cog',
    order=4
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
# CREAR PERMISOS
# ============================================================================


from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

def crear_permisos_basicos(app_label, model_name, nombre_amigable):
    ct = ContentType.objects.get(app_label=app_label, model=model_name)
    permisos = []
    for accion in ['view', 'add', 'change', 'delete']:
        codename = f"{accion}_{model_name}"
        name = f"Can {accion} {nombre_amigable}"
        permiso, _ = Permission.objects.get_or_create(
            codename=codename,
            content_type=ct,
            defaults={'name': name}
        )
        permisos.append(permiso)
    return permisos



# Permisos doctor app
# patient_perms = crear_permisos_basicos('doctor', 'patient', 'Paciente')
# diagnosis_perms = crear_permisos_basicos('doctor', 'diagnosis', 'Diagnóstico')

# Permisos seguridad
menu_perms = crear_permisos_basicos('security', 'menu', 'Menu')
module_perms = crear_permisos_basicos('security', 'module', 'Module')
user_perms = crear_permisos_basicos('security', 'user', 'User')
gmp_perms = crear_permisos_basicos('security', 'groupmodulepermission', 'GroupModulePermission')

# Permisos core
cargo_perms = crear_permisos_basicos('core', 'cargo', 'Cargo')
# especialidad_perms = crear_permisos_basicos('core', 'especialidadmedica', 'Especialidad Médica')
doctor_perms = crear_permisos_basicos('core', 'doctor', 'Doctor')
empleado_perms = crear_permisos_basicos('core', 'empleado', 'Empleado')



# ============================================================================
# ASIGNAR  PERMISOS
# ============================================================================

def asignar_permisos_a_grupo(grupo, modulo, permisos):
    gmp, created = GroupModulePermission.objects.get_or_create(group=grupo, module=modulo)
    if created or not gmp.permissions.exists():
        gmp.permissions.set(permisos)



# Médicos
# asignar_permisos_a_grupo(group_medicos, module1, patient_perms)
# asignar_permisos_a_grupo(group_medicos, module5, diagnosis_perms[:3])  # view, add, change
asignar_permisos_a_grupo(group_medicos, module2, [])
asignar_permisos_a_grupo(group_medicos, module3, [])
asignar_permisos_a_grupo(group_medicos, module6, [])

# Asistentes
# asignar_permisos_a_grupo(group_asistentes, module1, patient_perms[:2])  # view, add
asignar_permisos_a_grupo(group_asistentes, module4, [])
# asignar_permisos_a_grupo(group_asistentes, module5, [diagnosis_perms[0]])  # view
asignar_permisos_a_grupo(group_asistentes, module10, menu_perms)
asignar_permisos_a_grupo(group_asistentes, module11, module_perms)
asignar_permisos_a_grupo(group_asistentes, module12, user_perms)
asignar_permisos_a_grupo(group_asistentes, module13, gmp_perms)
asignar_permisos_a_grupo(group_asistentes, module14, [cargo_perms[0]])  # solo view
# asignar_permisos_a_grupo(group_asistentes, module15, especialidad_perms)
asignar_permisos_a_grupo(group_asistentes, module16, doctor_perms)
asignar_permisos_a_grupo(group_asistentes, module17, empleado_perms)



