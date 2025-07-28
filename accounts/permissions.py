from rest_framework.permissions import BasePermission

class IsCurrentAccessTokenForUser(BasePermission):
    """
    Allows access only if the JWT's JTI matches the one stored
    on the CustomUser model instance.
    """
    message = "This token is no longer valid. Please log in again."

    def has_permission(self, request, view):
        # The default IsAuthenticated permission already ran and set request.user
        if not request.user or not request.user.is_authenticated:
            return False

        # Get the JTI from the token payload
        token_jti = request.auth.get('jti')
        
        # Get the JTI stored on the user model itself
        # This is now a direct attribute access, no extra DB query!
        stored_jti = request.user.current_access_token_jti

        if not token_jti or token_jti != stored_jti:
            return False

        return True