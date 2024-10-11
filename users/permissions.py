'''
    Permission - Предназначены для дополнительной проверки прав доступа.
'''


from rest_framework import permissions

class IsModerators(permissions.BasePermission):
    ''' Функция кастомных прав доступа,
    которая проверяет входит ли users в состав group.moderators.
    '''

    def has_permission(self, request, view):
        return request.user.groups.filter(name="moderators").exists()


class IsOwner(permissions.BasePermission):
    ''' Функция кастомных прав доступа,
        которая проверяет является ли users == owner.
        '''

    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        return False