from django.urls import path
from .views import MyProtectedDataView


urlpatterns = [
    path('', MyProtectedDataView.as_view()),
    
]