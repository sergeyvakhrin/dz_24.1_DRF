from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import UserViewSet, PaymentsViewSet, UserCreateAPIView

app_name = UsersConfig.name

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')

router_payments = DefaultRouter()
router_payments.register(r'payments', PaymentsViewSet, basename='payments')

urlpatterns = [
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
] + router.urls + router_payments.urls

