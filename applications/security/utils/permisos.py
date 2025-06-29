from django.contrib.auth.models import Permission, ContentType
from django.apps import apps

def crear_permisos_basicos(app_label, model_name, nombre_amigable=""):
    """
    Crea los permisos básicos add, change, delete, view para un modelo.
    """
    permisos_creados = []

    try:
        model = apps.get_model(app_label, model_name)
    except LookupError:
        return []  # Modelo no existe

    content_type, created = ContentType.objects.get_or_create(
        app_label=app_label,
        model=model_name.lower(),
    )

    for codename, nombre in [
        ("add_" + model_name.lower(), f"Puede agregar {nombre_amigable}"),
        ("change_" + model_name.lower(), f"Puede modificar {nombre_amigable}"),
        ("delete_" + model_name.lower(), f"Puede eliminar {nombre_amigable}"),
        ("view_" + model_name.lower(), f"Puede ver {nombre_amigable}"),
    ]:
        perm, created = Permission.objects.get_or_create(
            codename=codename,
            content_type=content_type,
            defaults={"name": nombre}
        )
        permisos_creados.append(perm)

    return permisos_creados
