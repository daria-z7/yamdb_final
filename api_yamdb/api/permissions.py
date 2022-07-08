from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and (
            request.user.is_admin or request.user.is_superuser)


class IsAdminOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        return (
            request.method in SAFE_METHODS
            or (request.user.is_authenticated
                and (request.user.is_admin
                     or request.user.is_superuser)
                )
        )


class IsAuthorOrManagerOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        if request.method not in SAFE_METHODS:
            return request.user.is_authenticated
        return True

    def has_object_permission(self, request, view, obj):
        if request.method in ('PATCH', 'DELETE'):
            return (request.user == obj.author
                    or request.user.role
                    in (
                        request.user.MODERATOR,
                        request.user.ADMIN
                    )
                    or request.user.is_superuser)
        return True
