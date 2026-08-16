from rest_framework.permissions import BasePermission


class IsStaffUser(BasePermission):
    message = "Only staff users can manage the menu."

    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and request.user.is_staff
        )