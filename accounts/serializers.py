from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import AccessToken # Import AccessToken

class CustomUserTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        # This call creates the token pair and puts them into the 'data' dict.
        # This is the token that will be returned to the user.
        data = super().validate(attrs)

        # --- Corrected Logic ---
        # 1. Get the access token string from the data dictionary.
        access_token_str = data.get('access')

        if access_token_str:
            # 2. Decode the token string to get its payload, including the JTI.
            #    We use the AccessToken class for this.
            token = AccessToken(access_token_str)
            jti = token.get('jti')

            # 3. Save this correct JTI to the user model.
            self.user.current_access_token_jti = jti
            self.user.save()

        return data