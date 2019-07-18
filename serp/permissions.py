from rest_framework import permissions


class OwnedSearchResult(permissions.BasePermission):
    """ Custom permission to allow only user that executed search to see its results.
    """

    def has_object_permission(self, request, view, obj):
        # if search result have no owner - don't apply permission rules
        if obj.user == None:
            return True

        return obj.user == request.user
