from rest_framework import permissions

class IsOwnProfileOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.rec == request.user


class SeekervsRec(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return bool(request.user.is_rec)

# class IsAdminOrReadOnly(permissions.IsAdminUser):

#     def has_permission(self, request, view):
#         if request.method in permissions.SAFE_METHODS:
#             return True
#         else:
#             return bool(request.user and request.user.is_staff)
