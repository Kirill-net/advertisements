from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        # print(request.user, obj.creator)
        return request.user == obj.creator
