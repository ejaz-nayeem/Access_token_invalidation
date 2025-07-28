from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # AbstractUser provides username, email, password, etc.
    
    # --- YOUR CUSTOM FIELD ---
    # This will store the JTI of the one and only valid access token.
    # It can be null because a user might not have an active session.
    # It must be unique (if not null) because two users cannot have the same valid token.
    current_access_token_jti = models.CharField(
        max_length=255, 
        null=True, 
        blank=True, 
        unique=True, 
        db_index=True
    )

    def __str__(self):
        return self.username