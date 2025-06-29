from django.contrib.auth.models import Group

class SuperuserGroupSyncMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated and request.user.is_superuser:
            all_groups = Group.objects.all()
            if set(request.user.groups.all()) != set(all_groups):
                request.user.groups.set(all_groups)
        return self.get_response(request)
