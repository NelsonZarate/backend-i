from django.core.exceptions import PermissionDenied

class AdminRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_admin():
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class TeacherRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_teacher():
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)