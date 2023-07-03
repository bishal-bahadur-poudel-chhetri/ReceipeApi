from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from accounts.views import (
    RegisterAPIView,
    LogoutAPIView
    )

urlpatterns = [
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/', RegisterAPIView.as_view()),
    path('api/logout/', LogoutAPIView.as_view(), name='token_refresh'),


]