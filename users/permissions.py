from rest_framework import permissions


class IsModer(permissions.BasePermission):

    def has_permission(self, request, view):
        """ Проверяем на принадлежность к группе. """
        return request.user.groups.filter(name='Moderators').exists()


class IsOwner(permissions.BasePermission):
    """ Проверяем права на просмотр и редактирование. """
    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        return False
