from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView 

# --- Import YOUR custom login view from its correct location ---
from accounts.views import CustomUserLoginView 

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # --- This is the corrected line ---
    # It now points to YOUR view, which contains all your custom logic.
    path('api/token/', CustomUserLoginView.as_view(), name='token_obtain_pair'),
    
    # The refresh view can remain the default one.
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),    
    
    path('accounts/', include('accounts.urls')),
    path('myapp/', include('myapp.urls')),
]