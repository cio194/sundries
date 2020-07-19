# -*- coding: utf-8 -*-

from rest_framework import permissions


class IsOwnerOrReadOnly1(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """
    message = '您没有执行该操作的权限。'

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.is_staff and request.method == 'PATCH' and obj.author != request.user:
            return True
        if request.user.is_staff and request.method == 'PATCH' and obj.author == request.user:
            self.message = "您无法评论自己的周报"
            return False
        if not request.user.is_staff and request.method == 'PATCH':
            return False

        # Instance must have an attribute named `owner`.
        return obj.author == request.user


class IsOwnerOrReadOnly2(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.method == 'DELETE' and obj == request.user:
            return False

        # Instance must have an attribute named `owner`.
        return obj == request.user or request.user.is_staff


class IsOwnerOrReadOnly3(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        return obj.author == request.user


class IsAuthenticated1(permissions.BasePermission):
    """
    Allows access only to authenticated users.
    """
    message = '您没有执行该操作的权限。'

    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated and not request.user.is_admitted:
            self.message = '管理员还未同意您的申请'
        return bool(request.user and request.user.is_authenticated and request.user.is_admitted)


class IsAuthenticated2(permissions.BasePermission):
    """
    用户页面，未登录时只允许使用POST请求
    """
    message = '您没有执行该操作的权限。'

    def has_permission(self, request, view):
        if request.method == 'POST' and not (request.user and request.user.is_authenticated):
            return True
        if request.user and request.user.is_authenticated and not request.user.is_admitted:
            self.message = '管理员还未同意您的申请'
        return bool(request.user and request.user.is_authenticated and request.user.is_admitted)
