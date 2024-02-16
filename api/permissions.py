from rest_framework import permissions

class IsOwnerPermission(permissions.DjangoModelPermissions):
    
    authenticated_users_only = True
    
    def has_permission(self, request, view):
        return super().has_permission(request, view)

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user
    
    